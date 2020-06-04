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
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.template.loader import render_to_string
import smtplib
import json
import pickle
import os.path
import httplib2
import base64
import mimetypes
import csv
from django.http import FileResponse
from .models import locData,userdetail,ElsiCollegeDtls,ElsiTeacherDtls,TbtCollegeDtls,WorkshopDtls,WorkshopParticipants
from app.settings import EMAIL_HOST_USER,BASE_DIR,SCRIPTS_DIR

############################################################################################################################
import googlemaps
import requests
'''
API_KEY = 'AIzaSyD9qTJmiFUe3FQWlo5Z-A3l6pigxA3s8U8'
gmaps = googlemaps.Client(key = API_KEY)
print(gmaps)
url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
input='mbm Raj.'
other='&inputtype=textquery&fields=name'
result = requests.get(url+'input='+input+other+'&key='+API_KEY)
x = result.json()
print(x)
'''
# zero_results
# input='manganiram banghar memorial'
############################################################################################################################
# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.modify',
]

def form(request,uid):
    #print(request.GET['uid'])
    print(uid)
    return render(request,'form.html',context={'uuid':uid})

@api_view(['POST'])
def formdata(request):
    var = JSONParser().parse(request)
    print(var.get('name'),var.get('cname'),var.get('designation'),var.get('uuid'))
    return Response('success')

@api_view(['POST'])
def sendmail(request):
    obj = userdetail.objects.filter(emailid = '98dikshitajain@gmail.com')
    to = obj[0].emailid
    uuid = obj[0].id
    cc = ''
    bcc = '' 
    subject = 'Workshop Team Selection Form'
    body = render_to_string(os.path.join(SCRIPTS_DIR,'link.html'),{'uid':uuid})
    sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body)
    return JsonResponse({'status':'success'})

@api_view(['POST'])
def csvapprove(request):
    var = JSONParser().parse(request)
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        res = {}
        for row in r:
            if row[0] in var.get('list') :
                l=row[0]
                cc = row[1]
                bcc = row[1]
                if  len(row) > 7 :
                    body = row[-1]
                    subject = row[-2]
                else :
                    clg = row[5]
                    obj = ElsiCollegeDtls.objects.filter(college_name = clg)
                    res = getbody(clg,obj) 
                    subject = res['subject']
                    body = res['body']       
                sent = SendMessage(EMAIL_HOST_USER, l, cc, bcc, subject, body)
                print(l,sent)
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
        res = {}
        for row in r:
            if row[0] in var.get('list') :
                l=row[0]
                cc = row[1]
                bcc = row[1]
                attachmentFile = None
                if  len(row) > 7 :
                    body = row[-1]
                    subject = row[-2]
                else :
                    clg = row[5]
                    obj = ElsiCollegeDtls.objects.filter(college_name = clg)
                    res = getbody(clg,obj) 
                    subject = res['subject']
                    body = res['body'] 
                if attachmentFile:
                    pass
                    #message = createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachmentFile)
                else:
                    message = None
                    message = CreateMessageHtml(EMAIL_HOST_USER, l, cc, bcc, subject, body)
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
    obj = ElsiCollegeDtls.objects.filter(college_name = clg)
    file_path = os.path.join(BASE_DIR,'clgData.csv')
    f = open(file_path)
    reader = csv.DictReader(f)
    for rows in reader:
        if (rows['remail'] == rema):
            ccbcc = (rows['ccbcc'])
        #print(rows['remail'])
        #print(rema)
    d = {'to' : rema  ,'ccbcc' : ccbcc,'subject': '','body':'','attachments':''}
    res = getbody(clg,obj)
    d['subject'] = res['subject']
    d['body'] = res['body'] 
    d['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'} 
    return JsonResponse(d)

def getbody(clg,obj):
        try:
            district = "Not present"
            state = " Not present"
            c = ElsiCollegeDtls.objects.all()
            count=0
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            if obj.count() < 1:
                print('A')
                subject = "IIT Bombay, e-Yantra Lab Setup Initiative (eLSI): " +\
                    "Information for e-Yantra Lab Setup Initiative (eLSI): " +\
                     clg + " , " + district + " , " + state
                body = render_to_string(os.path.join(SCRIPTS_DIR,'a.html'),{'count':count})
            else :
                college_name = obj[0].college_name
                district = obj[0].district
                state = obj[0].state
                wo_attend = obj[0].wo_attend
                tbt_allowed = obj[0].tbt_allowed
                lab_inaugurated = obj[0].lab_inaugurated
                workshop = WorkshopParticipants.objects.filter(clg_id = obj[0].id)
                print(workshop.values())
                subject = "IIT Bombay, e-Yantra Lab Setup Initiative (eLSI): " +\
                        "Information for e-Yantra Lab Setup Initiative (eLSI): " +\
                        college_name + " , " + district + " , " + state
                if  obj[0].lab_inaugurated:
                    print('E')
                    det = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id )
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'elsi_college.html'),
                    {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                    'count':count,'datas':det})
                elif obj[0].wo_attend and obj[0].tbt_allowed:
                    tb = TbtCollegeDtls.objects.filter(elsi_clg_id = obj[0].id )
                    if tb[0].completed:
                        print('D')
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        details = ElsiTeacherDtls.objects.filter(id = workshop[0].tch_id )
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_complete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':det[0].start_date,'end_date':det[0].end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":details})
                    else:
                        print('C')
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        tch_id = workshop[0].tch_id
                        details = ElsiTeacherDtls.objects.filter(id = tch_id )
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_notcomplete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':det[0].start_date,'end_date':det[0].end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":details})
                elif obj[0].wo_attend :
                    print('B')
                    print(workshop.values())
                    workshop_id = workshop[0].workshop_id
                    workshop_dtl = WorkshopDtls.objects.filter(id = workshop_id)
                    print(workshop_dtl.values())
                    datas = ElsiTeacherDtls.objects.filter(id = workshop[0].tch_id )
                    clg_id = workshop_dtl[0].clg_id
                    temp = ElsiCollegeDtls.objects.filter(id = clg_id)
                    print(temp.values())
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'b.html'),
                    {'CollegeName':college_name,'State': state,'District':district,
                        'count':count,'start_date':workshop_dtl[0].start_date,'end_date':workshop_dtl[0].end_date,
                        'host_college':temp[0].college_name,'host_State':temp[0].state,'host_District':temp[0].district,
                        "datas":datas})
                else :
                    print('A')
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'a.html'),{'count':count})
            return {'subject':subject,'body':body}      
        except ValueError as e:
            return {'status':'failed','info':e.args[0]}   

@api_view(['POST'])
def save(request):
    var = JSONParser().parse(request)
    
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
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
            district = "Not present"
            state = " Not present"
            obj = ElsiCollegeDtls.objects.filter(college_name = clg)
            res = getbody(clg,obj)
            var['subject']=res['subject']
            var['body']=res['body']
            var['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
            return JsonResponse(var)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def getfile(request):
    var = JSONParser().parse(request)
    v = var.get('value')
    if v == 'Pamphlet2020.pdf':
        f = open(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'), 'rb')
        response = FileResponse(f)
        return response
    else:
        f = open(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'), 'rb')
        response = FileResponse(f)
        return response

@api_view(['POST'])
def awssubmit(request):
        try:
            var = JSONParser().parse(request)
            dict={}
            clist=[]
            state = var.get('state')
            districts = var.get('district')
            print(districts)
            obj1 = locData.objects.filter(locstate = state)
            if obj1.count() >= 1:
                for district in districts:
                    obj2 = locData.objects.filter(locdistrict = district)
                    if obj2.count() >= 1:
                        for rows in list(obj2.values()) :
                            clist = clist + [(rows['locemail'])]
                if len(clist) == 0:
                    return JsonResponse({'key':'nodata'})
                else:
                    dict['remail'] = clist
                    print(dict)
                    subject = "Send workshop Mail"
                    body = "heyyyyy"
                    dict['subject']=subject
                    dict['body']=body
                    return JsonResponse(dict)
                #var['attachments'] = None
            else:
                return JsonResponse({'key':'nodata'})
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def approve(request):
        try:
            var = JSONParser().parse(request)
            to = var.get('remail')
            cc = ','.join(map(str,var.get('ccbcc') ))
            bcc = ','.join(map(str,var.get('ccbcc') ))
            print(bcc)
            subject = var.get('subject')
            body = var.get('body')
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
    cc = ','.join(map(str,var.get('ccbcc') ))
    bcc = ','.join(map(str,var.get('ccbcc') ))
    subject = var.get('subject')
    body = var.get('body')
    credentials = get_credentials()
    attachmentFile=None
    result = None
    service = build('gmail', 'v1', credentials=credentials)
    if attachmentFile:
        pass
        #message = createMessageWithAttachment(sender, to, subject, msgHtml, msgPlain, attachmentFile)
    else:
        message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
    result = CreateDraft(service,"me",message)
    return JsonResponse({'status':'saved to draft'})

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
    file_path = os.path.join(SCRIPTS_DIR,'pickle.token')
    credentials_path=os.path.join(SCRIPTS_DIR,'credentials.json')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(host='127.0.0.1',port=8081)
            # Save the credentials for the next run
        with open(file_path, 'wb') as token:
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
    msg.attach(MIMEText(body, 'html'))
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