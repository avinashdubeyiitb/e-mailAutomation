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
from .models import clgData,tempCollegeData
from .serializers import ClgDataSerializer,TempSerializer
from app.settings import EMAIL_HOST_USER
# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

@api_view(['POST'])
<<<<<<< HEAD
def submit(request):
=======
def savefile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse({'key':'done'})

def base(info):
>>>>>>> refs/remotes/origin/master
        try:
            var = JSONParser().parse(request)
            clg = var.get('cname')
            tmpSrz = TempSerializer(data = var)
            obj = tempCollegeData.objects.filter(cname = clg)
            #print(obj.count(),obj)
            if obj.count()==0 :
                if tmpSrz.is_valid():
                    tmpSrz.save()    
                else :
                    return JsonResponse(tmpSrz.errors)       
            return JsonResponse({'status':'try for approve option'})
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def approve(request):
        try:        
            obj = tempCollegeData.objects.first()
            clg = getattr(obj, 'cname') 
            remail = getattr(obj,'remail')
            ccbcc = getattr(obj,'ccbcc')
            #print(clg,remail,ccbcc)
            tempCollegeData.objects.filter().delete() 
            obj = clgData.objects.filter(cname = clg)
            #print(obj,obj.count())
            if obj.count() >= 1:
                subject = "Send Information Mail"
                body = "You are already registered."
                email = EmailMessage(subject,body, EMAIL_HOST_USER, to=[remail], bcc=[ccbcc],
                        connection=None, attachments=None, headers=None, cc=[ccbcc],reply_to=None)
                sent = email.send()
                #print(sent,'!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if sent :      
                    return JsonResponse({'status':'success','info':'you are already registered'})
                else :
                    return JsonResponse({'status':'failure','info':'mail was not sent'})    
            else:
                clgSrz = ClgDataSerializer(data = {'cname' : clg})
                #print(clgSrz.is_valid(),clgSrz.errors,clgSrz)
                if clgSrz.is_valid():
                    clgSrz.save()
                subject = "Send Information Mail"
                body = "Welcome to our eyrc program."
                email = EmailMessage(subject,body, EMAIL_HOST_USER, to=[remail], bcc=[ccbcc],
                        connection=None, attachments=None, headers=None, cc=[ccbcc],reply_to=None)
                sent = email.send()
                #print(sent,'!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if sent :      
                    return JsonResponse({'status':'success','info':'you are now registered'})
                else :
                    return JsonResponse({'status':'failure','info':'mail was not sent'}) 
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
'''
def get(info):
    try :
        d=dict(json.loads(info.body))
        to = d['remail']
        sender = "intrnaakash@gmail.com"
        subject = "subject"
        msgHtml = ''
        data=collegeData.objects.get(college = d['cname'])
        with open('templates/registered.html', 'r') as email_content:
            msgHtml = email_content.read()
        msgPlain = "Hi\nPlain Email"
        SendMessage(sender, to, subject, msgHtml, msgPlain)
    except (NameError,ObjectDoesNotExist) as e :
        print(e.args[0])
        data = collegeData(mail_id = d['mail_id'],name = d['name'],designation = d['designation'],department = d['department'],college = d['college'],contact = d['contact'] )
        data.save('self')
        with open('templates/new.html', 'r') as email_content:
            msgHtml = email_content.read()
        msgPlain = "Hi\nPlain Email"
        SendMessage(sender, to, subject, msgHtml, msgPlain)

def SendMessage(sender, to, subject, msg, attachmentFile=None):
    #credentials = get_credentials()
    # http = credentials.authorize(httplib2.Http())
    # service = discovery.build('gmail', 'v1', http=http)
    #service = build('gmail', 'v1', credentials=credentials)
    if attachmentFile:
        pass
       #message1 = createMessageWithAttachment(sender, to, subject, msg,attachmentFile)
    else:
        message1 = CreateMessageHtml(sender, to, subject, msg)
    result = SendMessageInternal(service, "me", message1)
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
<<<<<<< HEAD
 '''   
def CreateMessageHtml(sender, to, subject, msg):
    message = MIMEText(msg)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = to
    #msg.attach(MIMEText(msgPlain, 'plain'))
    #msg.attach(MIMEText(msgHtml, 'html'))
=======

def CreateMessageHtml(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
>>>>>>> refs/remotes/origin/master
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
'''
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
'''