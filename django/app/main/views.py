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
from django.http import FileResponse,HttpResponse
from datetime import datetime
from django.utils.encoding import escape_uri_path
import smtplib
import json
import pickle
import os.path
import httplib2
import base64
import mimetypes
import email.encoders
import csv
from .models import userdetail,ElsiCollegeDtls,ElsiTeacherDtls,TbtCollegeDtls,WorkshopDtls,WorkshopParticipants,AICTE_list
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
###############################
# common functions
@api_view(['POST'])
def getfile(request):
    print('hii')
    var = JSONParser().parse(request)
    v = var.get('value')
    if v == 'Pamphlet2020.pdf':
        with open(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path('Pamphlet2020.pdf'))
            return response
    else:
        with open(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path('letter-of-intent.docx'))
            return response

def getbody(clg,obj,sta,dis):
        try:
            district = dis
            state = sta
            c = ElsiCollegeDtls.objects.all()
            count=0
            tchdtl = ['default']
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            if obj.count() < 1:
                print('A')
                subdiv = 'A'
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
                    subdiv = 'E'
                    l = ['sno.']
                    tchdtl2 = ['name','department','designation']
                    for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                    det = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id)
                    print(det)
                    d= {'data':[]}
                    for idx in range(det.count()):
                        d['data'].append({'id':det[idx].id,'value':[idx+1]})
                        for field in ElsiTeacherDtls._meta.fields:
                            if field.name in tchdtl2:
                                d['data'][idx]['value'].append(det.values()[idx][field.name])
                    print(d)
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'elsi_college.html'),
                    {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                    'count':count,"datas":d,'lst':l})
                elif obj[0].wo_attend and obj[0].tbt_allowed:
                    tb = TbtCollegeDtls.objects.filter(elsi_clg_id = obj[0].id )
                    if tb[0].completed:
                        print('D')
                        subdiv = 'D'
                        l = ['sno.']
                        tchdtl2 = ['name','department','designation']
                        for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        workshop_id = workshop[0].workshop_id
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        details = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                        print(details)
                        d= {'data':[]}
                        for idx in range(details.count()):
                            d['data'].append({'id':details[idx].id,'value':[idx+1]})
                            for field in ElsiTeacherDtls._meta.fields:
                                if field.name in tchdtl2:
                                    d['data'][idx]['value'].append(details.values()[idx][field.name])
                        print(d)
                        start_date = det[0].start_date
                        start_date = datetime.strptime(start_date, '%d-%m-%Y')
                        start_date = datetime.strftime(start_date,'%b %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%b %d, %Y')
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_complete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':start_date,'end_date':end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":d,'lst':l})
                    else:
                        print('C')
                        subdiv = 'C'
                        l = ['sno.']
                        tchdtl2 = ['name','department','designation']
                        for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        workshop_id = workshop[0].workshop_id
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        details = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                        print(details)
                        d= {'data':[]}
                        for idx in range(details.count()):
                            d['data'].append({'id':details[idx].id,'value':[idx+1]})
                            for field in ElsiTeacherDtls._meta.fields:
                                if field.name in tchdtl2:
                                    d['data'][idx]['value'].append(details.values()[idx][field.name])
                        print(d)
                        start_date = det[0].start_date
                        start_date = datetime.strptime(start_date, '%d-%m-%Y')
                        start_date = datetime.strftime(start_date,'%b %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%b %d, %Y')
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_notcomplete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':start_date,'end_date':end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":d,'lst':l})
                elif obj[0].wo_attend :
                    print('B')
                    subdiv = 'B'
                    l = ['sno.']
                    tchdtl2 = ['name','department']
                    for fields in ElsiTeacherDtls._meta.fields:
                        tchdtl.append(fields.name)
                        if fields.name in tchdtl2:
                            l.append(fields.name)
                    print(tchdtl)
                    print(workshop.values())
                    workshop_id = workshop[0].workshop_id
                    workshop_dtl = WorkshopDtls.objects.filter(id = workshop_id)
                    print(workshop_dtl.values())
                    datas = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                    print(datas.values())
                    d= {'data':[]}
                    for idx in range(datas.count()):
                        d['data'].append({'id':datas[idx].id,'value':[idx+1]})
                        for field in ElsiTeacherDtls._meta.fields:
                            if field.name in tchdtl2:
                                d['data'][idx]['value'].append(datas.values()[idx][field.name])
                    print(d)
                    clg_id = workshop_dtl[0].clg_id
                    temp = ElsiCollegeDtls.objects.filter(id = clg_id)
                    print(temp.values())
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'b.html'),
                    {'CollegeName':college_name,'State': state,'District':district,
                        'count':count,'host_college':temp[0].college_name,'host_State':temp[0].state,'host_District':temp[0].district,
                        "datas":d,'lst':l})
                else :
                    print('A')
                    subdiv = 'A'
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'a.html'),{'count':count})
            return {'subject':subject,'body':body,'subdiv':subdiv,'tchdtl':tchdtl}
        except ValueError as e:
            return {'status':'failed','info':e.args[0]}

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
        message = createMessageWithAttachment(sender, to,cc,bcc, subject,body, attachmentFile)
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
    msg['Bcc'] = bcc
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
    sender, to,cc,bcc, subject,body, attachmentFile):
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
    message['Bcc'] = bcc
    message['Cc'] = cc
    message['from'] = sender
    message['subject'] = subject

    messageA = MIMEMultipart('alternative')
    messageR = MIMEMultipart('related')

    messageR.attach(MIMEText(body, 'html'))
    # messageA.attach(MIMEText(msgPlain, 'plain'))
    messageA.attach(messageR)

    message.attach(messageA)

    print("create_message_with_attachment: file: %s" % attachmentFile)
    for attachment in attachmentFile :

        content_type, encoding = mimetypes.guess_type(attachment)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(attachment, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(attachment, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(attachment, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(attachment, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(attachment)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        email.encoders.encode_base64(msg)
        message.attach(msg)

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def getname(name):
    API_KEY = 'AIzaSyD9qTJmiFUe3FQWlo5Z-A3l6pigxA3s8U8'
    url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    input=name
    input.replace(" ", "%")
    other='&inputtype=textquery&fields=name'
    result = requests.get(url+'input='+input+other+'&key='+API_KEY)
    collx = result.json()
    return collx['candidates'][0]['name']
def getloc(name):
    API_KEY = 'AIzaSyD9qTJmiFUe3FQWlo5Z-A3l6pigxA3s8U8'
    url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    input=name
    input.replace(" ", "%")
    other='&inputtype=textquery&fields=formatted_address'
    result = requests.get(url+'input='+input+other+'&key='+API_KEY)
    collx = result.json()
    return collx
################################

################################
# send information mail
@api_view(['POST'])
def store(request):
        try:
            var = JSONParser().parse(request)
            clg = var.get('cname')
            district = var.get('district')
            state = var.get('state')
            tchdtl2 = var.get('tchdtl')
            subdiv = var.get('subdiv')
            tchdtl = ['default']
            if 'default' in tchdtl2:
                tchdtl2.remove('default')
                tchdtl2.append('name')
                tchdtl2.append('department')
                if subdiv in ['C','D','E']:
                    tchdtl2.append('designation')
            print(tchdtl2,district,state,clg)
            coll = getname(str(var.get('cname')))
            print(coll)
            if len(district) >0 and len(state)>0:
                dis = getname(str(var.get('district')))
                sta = getname(str(var.get('state')))
            else:
                collx = getloc(coll)
                data = collx['candidates'][0]['formatted_address']
                data.replace(" ", "")
                data = data.split(",")
                dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                print(dis)
                sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                print(sta)
            obj = ElsiCollegeDtls.objects.filter(college_name = clg)
            district = dis
            state = sta
            c = ElsiCollegeDtls.objects.all()
            count=0
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            if obj.count() < 1:
                pass
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
                    l = ['sno.']
                    for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                    det = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id )
                    print(det)
                    d= {'data':[]}
                    for idx in range(det.count()):
                        d['data'].append({'id':det[idx].id,'value':[idx+1]})
                        for field in ElsiTeacherDtls._meta.fields:
                            if field.name in tchdtl2:
                                d['data'][idx]['value'].append(det.values()[idx][field.name])
                    print(d)
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'elsi_college.html'),
                    {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                    'count':count,"datas":d,'lst':l})
                elif obj[0].wo_attend and obj[0].tbt_allowed:
                    tb = TbtCollegeDtls.objects.filter(elsi_clg_id = obj[0].id )
                    if tb[0].completed:
                        print('D')
                        l = ['sno.']
                        for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        workshop_id = workshop[0].workshop_id
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        details = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                        print(details)
                        d= {'data':[]}
                        for idx in range(details.count()):
                            d['data'].append({'id':details[idx].id,'value':[idx+1]})
                            for field in ElsiTeacherDtls._meta.fields:
                                if field.name in tchdtl2:
                                    d['data'][idx]['value'].append(details.values()[idx][field.name])
                        print(d)
                        start_date = det[0].start_date
                        start_date = datetime.strptime(start_date, '%d-%m-%Y')
                        start_date = datetime.strftime(start_date,'%b %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%b %d, %Y')
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_complete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':start_date,'end_date':end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":d,'lst':l})
                    else:
                        print('C')
                        l = ['sno.']
                        for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                        det = WorkshopDtls.objects.filter(clg_id = workshop[0].workshop_id )
                        workshop_id = workshop[0].workshop_id
                        temp = ElsiCollegeDtls.objects.filter(id = det[0].clg_id)
                        details = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                        print(details)
                        d= {'data':[]}
                        for idx in range(details.count()):
                            d['data'].append({'id':details[idx].id,'value':[idx+1]})
                            for field in ElsiTeacherDtls._meta.fields:
                                if field.name in tchdtl2:
                                    d['data'][idx]['value'].append(details.values()[idx][field.name])
                        print(d)
                        start_date = det[0].start_date
                        start_date = datetime.strptime(start_date, '%d-%m-%Y')
                        start_date = datetime.strftime(start_date,'%b %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%b %d, %Y')
                        body = render_to_string(os.path.join(SCRIPTS_DIR,'tbt_notcomplete.html'),
                        {'CollegeName':obj[0].college_name,'State': obj[0].state,'District':obj[0].district,
                        'count':count,'start_date':start_date,'end_date':end_date,'host_college':temp[0].college_name,'host_State':temp[0].state,
                        'host_District':temp[0].district,"datas":d,'lst':l})
                elif obj[0].wo_attend :
                    print('B')
                    l = ['sno.']
                    for fields in ElsiTeacherDtls._meta.fields:
                            tchdtl.append(fields.name)
                            if fields.name in tchdtl2:
                                l.append(fields.name)
                    print(workshop.values())
                    workshop_id = workshop[0].workshop_id
                    workshop_dtl = WorkshopDtls.objects.filter(id = workshop_id)
                    print(workshop_dtl.values())
                    datas = ElsiTeacherDtls.objects.filter(clg_id = obj[0].id,workshop_id = workshop_id)
                    print(datas)
                    d= {'data':[]}
                    for idx in range(datas.count()):
                        d['data'].append({'id':datas[idx].id,'value':[idx+1]})
                        for field in ElsiTeacherDtls._meta.fields:
                            if field.name in tchdtl2:
                                d['data'][idx]['value'].append(datas.values()[idx][field.name])
                    print(d)
                    clg_id = workshop_dtl[0].clg_id
                    temp = ElsiCollegeDtls.objects.filter(id = clg_id)
                    print(temp.values())
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'b.html'),
                    {'CollegeName':college_name,'State': state,'District':district,
                        'count':count,'host_college':temp[0].college_name,'host_State':temp[0].state,'host_District':temp[0].district,
                        "datas":d,'lst':l})
                else :
                    pass
            var['subject']=subject
            var['body']=body
            var['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
            var['subdiv'] = subdiv
            var['tchdtl'] = tchdtl
            return JsonResponse(var)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def csvapprove(request):
    sent = None
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        res = {}
        re = {}
        total = 0
        for row in r:
            if row[0] in request.data.get('list') :
                total = total + 1
                to=row[0]
                cc = row[1]
                bcc = row[2]
                district = (row[8])
                state = (row[7])
                attachmentFile = None
                if  len(row) > 10 :
                    body = row[-1]
                    subject = row[-2]
                else :
                    clg = row[6]
                    obj = ElsiCollegeDtls.objects.filter(college_name = clg)
                    coll = getname(clg)
                    print(coll)
                    if len(district) >0 and len(state)>0:
                        dis = getname(district)
                        sta = getname(state)
                    else:
                        data = collx['candidates'][0]['formatted_address']
                        data.replace(" ", "")
                        data = data.split(",")
                        dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                        print(dis)
                        sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                        print(sta)
                    res = getbody(clg,obj,sta,dis)
                    subject = res['subject']
                    body = res['body']
                if 'file1' in request.FILES and 'file2' in request.FILES:
                    file1=request.FILES['file1']
                    file2=request.FILES['file2']
                    #  Saving POST'ed file to storage
                    file_name1 = default_storage.save(file1.name, file1)
                    file_name2 = default_storage.save(file2.name, file2)
                    attachments = [os.path.join(BASE_DIR,file_name1),os.path.join(BASE_DIR,file_name2)]
                elif 'file1' in request.FILES :
                    file=request.FILES['file1']
                    #  Saving POST'ed file to storage
                    file_name = default_storage.save(file.name, file)
                    attachments = [os.path.join(BASE_DIR,file_name),os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
                elif 'file2' in request.FILES :
                    file=request.FILES['file2']
                    #  Saving POST'ed file to storage
                    file_name = default_storage.save(file.name, file)
                    attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),os.path.join(BASE_DIR,file_name)]
                else:
                    attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),
                    os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
                sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,attachments)
                if sent :
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("1")
                    else:
                      re["status"] = ["1"]
                    # res['msg'] = "mail sent successfully"
                else:
                    # res['msg'] = "failed to send mail"
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("0")
                    else:
                      re["status"] = ["0"]
    success = 0
    failure = 0
    for key,value in re.items():
        if key == 'status':
            for s in value:
                if s == "1":
                    success = success+1
                else:
                    failure = failure+1
    re['success'] = success
    re['failure'] =failure
    re['total'] = total
    print(re)
    return JsonResponse(re)

@api_view(['POST'])
def csvdraft(request):
    sent = None
    with open('scripts/info.json','r') as read:
        obj = json.load(read)
    file_path = obj['file_path']
    credentials = get_credentials()
    service = build('gmail', 'v1', credentials=credentials)
    with open(file_path,'r') as csvinput:
        r = csv.reader(csvinput)
        res = {}
        re = {}
        total = 0
        for row in r:
            if row[0] in request.data.get('list')  :
                total =total+1
                to=row[0]
                cc = row[1]
                bcc = row[2]
                district = (row[8])
                state = (row[7])
                attachmentFile = None
                if  len(row) > 10 :
                    body = row[-1]
                    subject = row[-2]
                else :
                    clg = row[6]
                    obj = ElsiCollegeDtls.objects.filter(college_name = clg)
                    coll = getname(clg)
                    print(coll)
                    if len(district) >0 and len(state)>0:
                        dis=getname(district)
                        sta = getname(state)
                    else:
                        data = collx['candidates'][0]['formatted_address']
                        data.replace(" ", "")
                        data = data.split(",")
                        dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                        print(dis)
                        sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                        print(sta)
                    res = getbody(clg,obj,sta,dis)
                    subject = res['subject']
                    body = res['body']
                if 'file1' in request.FILES and 'file2' in request.FILES:
                    file1=request.FILES['file1']
                    file2=request.FILES['file2']
                    #  Saving POST'ed file to storage
                    file_name1 = default_storage.save(file1.name, file1)
                    file_name2 = default_storage.save(file2.name, file2)
                    attachments = [os.path.join(BASE_DIR,file_name1),os.path.join(BASE_DIR,file_name2)]
                elif 'file1' in request.FILES :
                    file=request.FILES['file1']
                    #  Saving POST'ed file to storage
                    file_name = default_storage.save(file.name, file)
                    attachments = [os.path.join(BASE_DIR,file_name),os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
                elif 'file2' in request.FILES :
                    file=request.FILES['file2']
                    #  Saving POST'ed file to storage
                    file_name = default_storage.save(file.name, file)
                    attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),os.path.join(BASE_DIR,file_name)]
                else:
                    attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),
                    os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
                attachmentFile = attachments
                if attachmentFile:
                    message = createMessageWithAttachment(EMAIL_HOST_USER, to,cc,bcc, subject,body, attachmentFile)
                else:
                    message = None
                    message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
                result = CreateDraft(service,"me",message)
                if result :
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("1")
                    else:
                      re["status"] = ["1"]
                    # res['msg'] = "mail sent successfully"
                else:
                    # res['msg'] = "failed to send mail"
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("0")
                    else:
                      re["status"] = ["0"]
    success = 0
    failure = 0
    for key,value in re.items():
        if key == 'status':
            for s in value:
                if s == "1":
                    success = success+1
                else:
                    failure = failure+1
    re['success'] = success
    re['failure'] =failure
    re['total'] = total
    print(re)
    return JsonResponse(re)

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
            cc = (rows['cc'])
            bcc = (rows['bcc'])
            district = (rows['district'])
            state = (rows['state'])
    coll = getname(var.get('cname'))
    print(coll)
    if len(district) >0 and len(state)>0:
        dis=getname(district)
        sta=getname(state)
    else:
        collx = getloc(coll)
        data = collx['candidates'][0]['formatted_address']
        data.replace(" ", "")
        data = data.split(",")
        dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
        print(dis)
        sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
        print(sta)
    d = {'to' : rema  ,'cc' : cc,'bcc' : bcc,'subject': '','body':'','attachments':''}
    res = getbody(clg,obj,sta,dis)
    d['subject'] = res['subject']
    d['body'] = res['body']
    d['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
    d['attachmentlinks'] = {'pamp':'https://www.e-yantra.org/img/Pamphlet2020.pdf','LoI':'http://elsi.e-yantra.org/eyrtc/downloads/loi'}
    return JsonResponse(d)

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
            district = var.get('district')
            state = var.get('state')
            coll = getname(var.get('cname'))
            print(coll)
            if len(district) >0 and len(state)>0:
                dis=getname(str(var.get('district')))
                sta=getname(str(var.get('state')))
            else:
                collx = getloc(coll)
                data = collx['candidates'][0]['formatted_address']
                data.replace(" ", "")
                data = data.split(",")
                dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                print(dis)
                sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                print(sta)
            obj = ElsiCollegeDtls.objects.filter(college_name = clg)
            res = getbody(clg,obj,sta,dis)
            var['subject']=res['subject']
            var['body']=res['body']
            var['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
            var['attachmentlinks'] = {'pamp':'https://www.e-yantra.org/img/Pamphlet2020.pdf','LoI':'http://elsi.e-yantra.org/eyrtc/downloads/loi'}
            var['subdiv'] = res['subdiv']
            var['tchdtl'] = res['tchdtl']
            return JsonResponse(var)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def approve(request):
        try:
            to = request.data.get('remail')
            if type(request.data.get('cc')) == list:
                cc = ','.join(map(str,request.data.get('cc') ))
            else:
                cc = request.data.get('cc')
            if type(request.data.get('bcc')) == list:
                bcc = ','.join(map(str,request.data.get('bcc') ))
            else:
                bcc = request.data.get('bcc')
            subject = request.data.get('subject')
            body = request.data.get('body')
            sent = None
            if 'file1' in request.FILES and 'file2' in request.FILES:
                file1=request.FILES['file1']
                file2=request.FILES['file2']
                #  Saving POST'ed file to storage
                file_name1 = default_storage.save(file1.name, file1)
                file_name2 = default_storage.save(file2.name, file2)
                attachments = [os.path.join(BASE_DIR,file_name1),os.path.join(BASE_DIR,file_name2)]
            elif 'file1' in request.FILES :
                file=request.FILES['file1']
                #  Saving POST'ed file to storage
                file_name = default_storage.save(file.name, file)
                attachments = [os.path.join(BASE_DIR,file_name),os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
            elif 'file2' in request.FILES :
                file=request.FILES['file2']
                #  Saving POST'ed file to storage
                file_name = default_storage.save(file.name, file)
                attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),os.path.join(BASE_DIR,file_name)]
            else:
                attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),
                os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,attachments)
            if sent :
                return JsonResponse({'status':'success','info':'mail sent successfully'})
            else :
                return JsonResponse({'status':'failure','info':'mail was not sent'})
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def gsave(request):
    to = request.data.get('remail')
    if type(request.data.get('cc')) == list:
        cc = ','.join(map(str,request.data.get('cc') ))
    else:
        cc = request.data.get('cc')
    if type(request.data.get('bcc')) == list:
        bcc = ','.join(map(str,request.data.get('bcc') ))
    else:
        bcc = request.data.get('bcc')
    subject = request.data.get('subject')
    body = request.data.get('body')
    sent = None
    if 'file1' in request.FILES and 'file2' in request.FILES:
        file1=request.FILES['file1']
        file2=request.FILES['file2']
        #  Saving POST'ed file to storage
        file_name1 = default_storage.save(file1.name, file1)
        file_name2 = default_storage.save(file2.name, file2)
        attachments = [os.path.join(BASE_DIR,file_name1),os.path.join(BASE_DIR,file_name2)]
    elif 'file1' in request.FILES :
        file=request.FILES['file1']
        #  Saving POST'ed file to storage
        file_name = default_storage.save(file.name, file)
        attachments = [os.path.join(BASE_DIR,file_name),os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
    elif 'file2' in request.FILES :
        file=request.FILES['file2']
        #  Saving POST'ed file to storage
        file_name = default_storage.save(file.name, file)
        attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),os.path.join(BASE_DIR,file_name)]
    else:
        attachments = [os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'),os.path.join(SCRIPTS_DIR,'letter-of-intent.docx')]
    credentials = get_credentials()
    attachmentFile=attachments
    result = None
    service = build('gmail', 'v1', credentials=credentials)
    if attachmentFile:
        message = createMessageWithAttachment(EMAIL_HOST_USER, to,cc,bcc, subject, body, attachmentFile)
    else:
        message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
    result = CreateDraft(service,"me",message)
    return JsonResponse({'status':'saved to draft'})
######################

######################
#workshop announcement
@api_view(['POST'])
def awssubmit(request):
        try:
            var = JSONParser().parse(request)
            dict={}
            clist=[]
            hcn = var.get('hcn')
            getdet = ElsiCollegeDtls.objects.filter(college_name = hcn)
            startdate = var.get('startdate')
            enddate = var.get('enddate')
            startdate = datetime.strptime(startdate, '%Y-%m-%d')
            day1 = startdate.strftime("%A")
            startdate = datetime.strftime(startdate,'%b %d, %Y')
            enddate = datetime.strptime(enddate, '%Y-%m-%d')
            day2 = enddate.strftime("%A")
            enddate = datetime.strftime(enddate,'%b %d, %Y')
            venueadd = var.get('venueadd')
            cooname = var.get('cooname')
            cooemail = var.get('cooemail')
            coono = var.get('coono')
            state = var.get('state')
            districts = var.get('district')
            c = ElsiCollegeDtls.objects.all()
            count=0
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            obj1 = ElsiCollegeDtls.objects.filter(state = state)
            if obj1.count() >= 1:
                for district in districts:
                    obj2 = ElsiCollegeDtls.objects.filter(district = district)
                    if obj2.count() >= 1:
                        for rows in list(obj2.values()) :
                            clist = clist + [(rows['college_name'])]
                if len(clist) == 0:
                    return JsonResponse({'key':'nodata'})
                else:
                    dict['bcc'] = clist
                    print(dict)
                    subject = "IIT Bombay, e-Yantra Lab Setup Initiative (eLSI): +\
                     Invitation to Attend the Two Day Workshop at " + hcn +", " + getdet[0].district +", " + getdet[0].state
                    body = render_to_string(os.path.join(SCRIPTS_DIR,'announce_workshop.html'),
                    {'venueadd':venueadd,'cooname': cooname,'cooemail':cooemail, 'coono':coono, 'hcn':hcn ,'hcnstate':getdet[0].state,
                        'hcndistrict':getdet[0].district,'count':count,'startdate':startdate,'enddate':enddate,'day1':day1,'day2':day2})
                    dict['subject']=subject
                    dict['body']=body
                    dict['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
                    dict['attachmentlinks'] = {'pamp':'https://www.e-yantra.org/img/Pamphlet2020.pdf','LoI':'http://elsi.e-yantra.org/eyrtc/downloads/loi'}
                    return JsonResponse(dict)
            else:
                return JsonResponse({'key':'nodata'})
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})
######################

######################
# workshop team algo
@api_view(['POST'])
def mailids(request):
    objs = userdetail.objects.all()
    print(objs)
    l = []
    for idx in range(objs.count()):
        l.append(objs[idx].emailid)
    print(l)
    return JsonResponse({'mailids':l})

def form(request,uid):
    return render(request,'form.html',context={'uuid':uid})

@api_view(['POST'])
def formdata(request):
    var = JSONParser().parse(request)
    print(var.get('name'),var.get('cname'),var.get('designation'),var.get('uuid'))
    return Response('success')

@api_view(['POST'])
def sendmail(request):
    objs = userdetail.objects.all()
    for idx in range(objs.count()):
        to = objs[idx].emailid
        uuid = objs[idx].id
        cc = ''
        bcc = ''
        subject = 'Workshop Team Selection Form'
        body = render_to_string(os.path.join(SCRIPTS_DIR,'link.html'),{'uid':uuid})
        sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body)
    return JsonResponse({'status':'success'})
######################
