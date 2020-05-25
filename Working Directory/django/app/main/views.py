from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from rest_framework.parsers import JSONParser
from django.core.mail import EmailMessage
from django.http.response import JsonResponse
import smtplib
import json
import pickle
import os.path
import httplib2
import base64
import mimetypes
import csv
from django.core.files.storage import default_storage

from .models import clgData
from .serializers import ClgDataSerializer
from app.settings import EMAIL_HOST_USER,BASE_DIR
# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.modify',
]

@api_view(['POST'])
def csvapprove(request):
    var = JSONParser().parse(request)
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        all=[]
        res = {}
        for row in r:
            if row[0] in var.get('list') :
                l=row[0]
                body = None
                subject = None
                sent = None
                if  len(row) > 7 :
                    body = row[-1]
                    subject = row[-2]
                obj = clgData.objects.filter(cname = row[5])
                if obj.count() >= 1:
                    if body == None :
                        body = "You are already registered"
                        subject = "Send Information Mail"
                else:
                    clgSrz = ClgDataSerializer(data = {'cname' : row[5]})
                    if clgSrz.is_valid():
                        clgSrz.save()
                    if body == None :
                        body = "Welcome to our eyrc program."
                        subject = "Send Information Mail"
                sent = SendMessage(EMAIL_HOST_USER,l,row[1],row[1], subject, body)
                #print(l,sent)
                if sent :
                    res[l] = "mail sent successfully"
                else:
                    res[l] = "failed to send mail"
        return JsonResponse(res)

@api_view(['POST'])
def csvdraft(request):
    var = JSONParser().parse(request)
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    credentials = get_credentials()
    service = build('gmail', 'v1', credentials=credentials)
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        all=[]
        res = {}
        for row in r:
            if row[0] in var.get('list') :
                l=row[0]
                body = None
                subject = None
                result = None
                attachmentFile = None
                if  len(row) > 7 :
                    body = row[-1]
                    subject = row[-2]
                obj = clgData.objects.filter(cname = row[5])
                if obj.count() >= 1:
                    if body == None :
                        body = "You are already registered"
                        subject = "Send Information Mail"
                else:
                    if body == None :
                        body = "Welcome to our eyrc program."
                        subject = "Send Information Mail"
                if attachmentFile:
                    pass
                    #message = createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachmentFile)
                else:
                    message = CreateMessageHtml(EMAIL_HOST_USER,l,row[1],row[1], subject, body)
                result = CreateDraft(service,"me",message)
                if result :
                    res[l] = "saved to draft"
                else :
                    res[l] = "failed to save to draft"
        return JsonResponse(res)

@api_view(['POST'])
def idrequest(request):
    var = JSONParser().parse(request)
    clg = var.get('cname')
    rema = var.get('remail')
    obj = clgData.objects.filter(cname = clg)
    file_path = os.path.join(BASE_DIR,'clgData.csv')
    f = open(file_path)
    reader = csv.DictReader(f)
    for rows in reader:
        if (rows['remail'] == rema):
            ccbcc = (rows['ccbcc'])
        #print(rows['remail'])
        #print(rema)
    d = {'to' : rema  ,'ccbcc' : ccbcc,'subject': '','body':''}
    if obj.count() >= 1:
        subject = "Send Information Mail"
        body = "You are already registered."
        d['subject']=subject
        d['body']=body
    else:
        subject = "Send Information Mail"
        body = "Welcome to our eyrc program."
        d['subject']=subject
        d['body']=body
    return JsonResponse(d)

@api_view(['POST'])
def save(request):
    var = JSONParser().parse(request)
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    write_path = os.path.join(BASE_DIR,'test.csv')
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        all=[]
        for row in r:
            if row[0] == 'remail':
                row.append('body')
                row.append('subject')
            elif row[0] == var.get('remail') :
                row[1] = var.get('ccbcc')
                row.append(var.get('subject'))
                row.append(var.get('body'))
            all.append(row)
        with open(file_path, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            writer.writerows(all)
    return JsonResponse({'status':'saved'})

@api_view(['POST'])
def csvsubmit(request):
    file = request.FILES['file']
    if os.path.getsize('scripts/info.json') :
        with open('scripts/info.json','r') as read:
            obj = json.load(read)
            os.remove(obj['file_name'])
    file_name = default_storage.save(file.name,file)
    CSV_DIR = os.path.join(BASE_DIR,file_name)
    with open('scripts/info.json','w') as write :
        json.dump({'file_path':CSV_DIR,'file_name':file_name},write)
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        clist = []
        for rows in reader :
            clist = clist + [(rows['cname'],rows['remail'])]
        return JsonResponse(dict(clist))

@api_view(['POST'])
def submit(request):
        try:
            var = JSONParser().parse(request)
            clg = var.get('cname')
            obj = clgData.objects.filter(cname = clg)
            if obj.count() >= 1:
                subject = "Send Information Mail"
                body = "You are already registered."
                var['subject']=subject
                var['body']=body
                #var['attachments'] = None
            else:
                clgSrz = ClgDataSerializer(data = {'cname' : clg})
                if clgSrz.is_valid():
                    clgSrz.save()
                subject = "Send Information Mail"
                body = "Welcome to our eyrc program."
                var['subject']=subject
                var['body']=body
                #var['attachments'] = 'scripts/letter-of-intent.docx'
            return JsonResponse(var)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def approve(request):
        try:
            var = JSONParser().parse(request)
            to = var.get('remail')
            cc = var.get('ccbcc')
            bcc = var.get('ccbcc')
            subject = var.get('subject')
            body = var.get('body')
            #attachments = var.get('attachments')
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body)
            if sent :
                return JsonResponse({'status':'success','info':'mail sent successfully'})
            else :
                return JsonResponse({'status':'failure','info':'mail was not sent'})
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def gsave(request):
    var = JSONParser().parse(request)
    to = var.get('remail')
    cc = var.get('ccbcc')
    bcc = var.get('ccbcc')
    subject = var.get('subject')
    body = var.get('body')
    credentials = get_credentials()
    attachmentFile=None
    service = build('gmail', 'v1', credentials=credentials)
    if attachmentFile:
        pass
        #message = createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachmentFile)
    else:
        message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
    result = CreateDraft(service,"me",message)
    return JsonResponse(result)

def CreateDraft(service, user_id, message_body):
  """Create and insert a draft email. Print the returned draft's message and id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message_body: The body of the email message, including headers.

  Returns:
    Draft object, including draft id and message meta data.
  """
  try:
    message = {'message': message_body}
    draft = service.users().drafts().create(userId=user_id, body=message).execute()
    print('Draft id: %s\nDraft message: %s' % (draft['id'], draft['message']))
    return draft
  except errors.HttpError as error:
    print('An error occurred: %s' % error)
    return error

def SendMessage(sender, to, cc, bcc, subject, body, attachmentFile=None):
    credentials = get_credentials()
    service = build('gmail', 'v1', credentials=credentials)
    #msgPlain = body
    #with open('templates/new.html' ,'r') as email_content:
        #msgHtml = email_content.read()
    if attachmentFile:
        pass
        #message = createMessageWithAttachment(sender, to, subject, msgPlain, msgHtml, attachmentFile)
    else:
        message = CreateMessageHtml(sender, to, cc, bcc, subject, body)
    result = SendMessageInternal(service, "me", message)
    return result

def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    #file_path = os.path.join(SETTINGS_DIR,'pickle.token')
    #credentials_path=os.path.join(STATIC_DIR,'credentials.json')
    if os.path.exists('scripts/pickle.token'):
        with open('scripts/pickle.token', 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(host='127.0.0.1',port=8081)
            # Save the credentials for the next run
        with open('pickle.token', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def CreateMessageHtml(sender, to, cc, bcc, subject, body, msgHtml=None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['Bcc'] = cc
    msg['To'] = to
    msg['Cc'] = cc
    #msg['Bcc'] = bcc
    #with open('templates/new.html', 'r') as email_content:
        #msgHtml = email_content.read()
    msg.attach(MIMEText(body, 'plain'))
    #msg.attach(MIMEText(msgHtml, 'html'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string().encode()).decode()}

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return "Error"
    return "OK"

def createMessageWithAttachment(
    sender, to, subject, msgHtml, msgPlain, attachmentFile):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      msgHtml: Html message to be sent
      msgPlain: Alternative plain text message for older email clients
      attachmentFile: The path to the file to be attached.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEMultipart('mixed')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    messageA = MIMEMultipart('alternative')
    messageR = MIMEMultipart('related')

    messageR.attach(MIMEText(msgHtml, 'html'))
    messageA.attach(MIMEText(msgPlain, 'plain'))
    messageA.attach(messageR)

    message.attach(messageA)

    print("create_message_with_attachment: file: %s" % attachmentFile)
    content_type, encoding = mimetypes.guess_type(attachmentFile)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(attachmentFile, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(attachmentFile, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(attachmentFile, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(attachmentFile, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(attachmentFile)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
