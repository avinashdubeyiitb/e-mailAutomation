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
import operator
import pickle
import os.path
import httplib2
import base64
import mimetypes
import email.encoders
import csv
from .serializers import *
from .models import *
from app.settings import EMAIL_HOST_USER,BASE_DIR,SCRIPTS_DIR
######################

# from django.contrib.auth.decorators import login_required
#
# @login_required
# def home(request):
#     return render(request, os.path.join(SCRIPTS_DIR,'home.html'))
#
# def login(request):
#     return render(request, os.path.join(SCRIPTS_DIR,'login.html'))
#
# def logout(request):
#     return render(request, os.path.join(SCRIPTS_DIR,'logout.html'))
#
# def public(request):
#     return HttpResponse("You don't need to be authenticated to see this")
#
#
# @api_view(['GET'])
# def private(request):
#     return HttpResponse("You should not see this message if not authenticated!")
#####################
############################################################################################################################
import googlemaps
import requests
#
# API_KEY = 'AIzaSyD9qTJmiFUe3FQWlo5Z-A3l6pigxA3s8U8'
# gmaps = googlemaps.Client(key = API_KEY)
# print(gmaps)
# url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
# input='mbm Raj.'
# other='&inputtype=textquery&fields=name'
# result = requests.get(url+'input='+input+other+'&key='+API_KEY)
# x = result.json()
# print(x)
#

# zero_results
# input='manganiram banghar memorial'
############################################################################################################################

# result = requests.get('https://api.foursquare.com/v2/venues/search'+'&client_id='+'JXAUNDUQSLCQVQRJER3CHDXY2SYR3EVCB5UT3D3Q340JWJJI'
#  + '&client_secret=' + '4SCOWU5XHQIG2RYIDEI1HRBV32A11EJ4YFQKCJO2G4DZISRF')
# x = result.json()
# print(x)



###########################################################################################################################
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
                        det = WorkshopDtls.objects.filter(id = workshop[0].workshop_id )
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
                        start_date = datetime.strftime(start_date,'%B %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%B %d, %Y')
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
                        det = WorkshopDtls.objects.filter(id = workshop[0].workshop_id )
                        print(det.values())
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
                        start_date = datetime.strftime(start_date,'%B %d, %Y')
                        end_date = det[0].end_date
                        end_date = datetime.strptime(end_date, '%d-%m-%Y')
                        end_date = datetime.strftime(end_date,'%B %d, %Y')
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
    print(collx)
    if collx['status'] == 'REQUEST_DENIED':
        return name
    else:
        return collx['candidates'][0]['name']
def getloc(name):
    API_KEY = 'AIzaSyBE-9YyXHa6tXkOFmZpNS3fdXkSwU2bMk8'
    url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    input=name
    input.replace(" ", "%")
    other='&inputtype=textquery&fields=formatted_address'
    result = requests.get(url+'input='+input+other+'&key='+API_KEY)
    collx = result.json()
    print(collx)
    if collx['status'] == 'REQUEST_DENIED':
        return name
    else:
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
                        det = WorkshopDtls.objects.filter(id = workshop[0].workshop_id )
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
                        det = WorkshopDtls.objects.filter(id = workshop[0].workshop_id )
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
                        files2send2 = list(request.data.get('files2send2').split(","))
                        print(files2send2)
                        attachments = []
                        for f in files2send2:
                            if f == 'Pamphlet2020.pdf':
                                attachments.append(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'))
                            elif f == 'letter-of-intent.docx':
                                attachments.append(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'))
                        if 'file2' in request.FILES :
                            file=request.FILES['file2']
                            #  Saving POST'ed file to storage
                            file_name = default_storage.save(file.name, file)
                            attachments.append(os.path.join(BASE_DIR,file_name))
                            print(attachments)
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
    if 'file2' in request.FILES :
        os.remove(os.path.join(BASE_DIR,file_name))
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
                    files2send2 = list(request.data.get('files2send2').split(","))
                    print(files2send2)
                    attachments = []
                    for f in files2send2:
                        if f == 'Pamphlet2020.pdf':
                            attachments.append(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'))
                        elif f == 'letter-of-intent.docx':
                            attachments.append(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'))
                    if 'file2' in request.FILES :
                        file=request.FILES['file2']
                        #  Saving POST'ed file to storage
                        file_name = default_storage.save(file.name, file)
                        attachments.append(os.path.join(BASE_DIR,file_name))
                        print(attachments)
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
    if 'file2' in request.FILES :
        os.remove(os.path.join(BASE_DIR,file_name))
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
            #print(request.data.get('file1'))
            #print(request.data.get('file2'))
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
            files2send1 = list(request.data.get('files2send1').split(","))
            print(files2send1)
            attachments = []
            for f in files2send1:
                if f == 'Pamphlet2020.pdf':
                    attachments.append(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'))
                elif f == 'letter-of-intent.docx':
                    attachments.append(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'))
            if 'file1' in request.FILES :
                file=request.FILES['file1']
                #  Saving POST'ed file to storage
                file_name = default_storage.save(file.name, file)
                attachments.append(os.path.join(BASE_DIR,file_name))
            print(attachments)
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,attachments)
            if 'file1' in request.FILES :
                os.remove(os.path.join(BASE_DIR,file_name))
            if sent :
                return JsonResponse({'status':'success','info':'mail sent successfully'})
            else :
                return JsonResponse({'status':'failure','info':'mail was not sent'})
            #return JsonResponse({'status':'success'})
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
    files2send1 = list(request.data.get('files2send1').split(","))
    print(files2send1)
    attachments = []
    for f in files2send1:
        if f == 'Pamphlet2020.pdf':
            attachments.append(os.path.join(SCRIPTS_DIR,'Pamphlet2020.pdf'))
        elif f == 'letter-of-intent.docx':
            attachments.append(os.path.join(SCRIPTS_DIR,'letter-of-intent.docx'))
        if 'file1' in request.FILES :
            file=request.FILES['file1']
            #  Saving POST'ed file to storage
            file_name = default_storage.save(file.name, file)
            attachments.append(os.path.join(BASE_DIR,file_name))
        print(attachments)
    credentials = get_credentials()
    attachmentFile=attachments
    result = None
    service = build('gmail', 'v1', credentials=credentials)
    if attachmentFile:
        message = createMessageWithAttachment(EMAIL_HOST_USER, to,cc,bcc, subject, body, attachmentFile)
    else:
        message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
    result = CreateDraft(service,"me",message)
    if 'file1' in request.FILES :
        os.remove(os.path.join(BASE_DIR,file_name))
    return JsonResponse({'status':'saved to draft'})
######################

######################
#workshop announcement
@api_view(['POST'])
def cwssubmit(request):
        try:
            var = JSONParser().parse(request)
            serializer = CreateWorkshop(data=var)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                print('done')
                return JsonResponse({'status': 'Created Successfully'})
            else:
                print('failure')
                return JsonResponse({'status': 'Problem in Serializing'})
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def getwrklist(request):
        try:
            obj = create_workshop.objects.all()
            wrklist = {}
            for i in range(obj.count()):
                if "list" in wrklist:
                    wrklist["list"].append(obj[i].hcn)
                else:
                    wrklist["list"] = [obj[i].hcn]
            print(wrklist)
            return JsonResponse(wrklist)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def awssubmit(request):
        try:
            var = JSONParser().parse(request)
            selectedworkshop = var.get('selectedworkshop')
            wrkdet = create_workshop.objects.filter(hcn = selectedworkshop)
            dict={}
            clist=[]
            hcn = wrkdet[0].hcn
            getdet = ElsiCollegeDtls.objects.filter(college_name = hcn)
            startdate = wrkdet[0].startdate
            enddate = wrkdet[0].enddate
            filldate = var.get('filldate')
            startdate = datetime.strptime(startdate, '%Y-%m-%d')
            day1 = startdate.strftime("%A")
            startdate = datetime.strftime(startdate,'%B %d, %Y')
            enddate = datetime.strptime(enddate, '%Y-%m-%d')
            day2 = enddate.strftime("%A")
            enddate = datetime.strftime(enddate,'%B %d, %Y')
            filldate = datetime.strptime(filldate, '%Y-%m-%d')
            filldate = datetime.strftime(filldate,'%B %d, %Y')
            venueadd = wrkdet[0].venueadd
            cooname = wrkdet[0].cooname
            cooemail = wrkdet[0].cooemail
            coono = wrkdet[0].coono
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
                        'hcndistrict':getdet[0].district,'count':count,'startdate':startdate,'enddate':enddate,'day1':day1,'day2':day2,'filldate':filldate})
                    dict['subject']=subject
                    dict['body']=body
                    dict['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
                    dict['attachmentlinks'] = {'pamp':'https://www.e-yantra.org/img/Pamphlet2020.pdf','LoI':'http://elsi.e-yantra.org/eyrtc/downloads/loi'}
                    return JsonResponse(dict)
            else:
                return JsonResponse({'key':'nodata'})
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def awsedit(request):
    var = JSONParser().parse(request)
    sw = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = sw)
    data = {
        'hcn':sw,'startdate':wrkshp[0].startdate,
        'enddate':wrkshp[0].enddate,'venueadd':wrkshp[0].venueadd,
        'cooname':wrkshp[0].cooname,'cooemail':wrkshp[0].cooemail,
        'coono':wrkshp[0].coono,'wid':wrkshp[0].id
    }
    return JsonResponse(data)

@api_view(['POST'])
def awssave(request):
    var = JSONParser().parse(request)
    data = create_workshop.objects.filter(id = var.get('wid'))
    print(data.values())
    data.update(hcn = var.get('hcn'),startdate = var.get('startdate'),
        enddate = var.get('enddate'),venueadd = var.get('venueadd'),
        cooname = var.get('cooname'),cooemail = var.get('cooemail'),
        coono = var.get('coono'))
    print(data.values())
    return JsonResponse({'status':'saved'})

######################

######################
# workshop team algo

def algo_for_available_mem(spl_mem_available,workshop_lead,ranked_data,availcriteria,lang,tcntt):
    print('here are available members')
    msg = 'These people are special cases'
    availctr = []
    for i in availcriteria:
        if i == 'Highest Count of Workshop in Past Running Year':
            availctr.append(0)
        elif i == 'Linguistics Criteria':
            availctr.append(3)
        elif i == 'Count of Total Workshop':
            availctr.append(2)
    print(availctr)
    p = WorkshopsTakenCount.objects.all()
    d=[]
    def sort_table(table, cols):
        for col in reversed(cols):
            table = sorted(table, key=operator.itemgetter(col))
        return table
    for i in range(p.count()):
        for j in range(len(spl_mem_available)):
            if spl_mem_available[j] == p[i].name:
                d.append([p[i].past_year, p[i].name,p[i].total_count])
    for i in range(len(d)):
        lang_data = userdetail.objects.filter(name = d[i][1])
        if lang_data[0].language is None:
            d[i].extend('1')
        else:
            l = lang_data[0].language.split(',')
            for j in l :
                print(j)
                if j == lang:
                    d[i].extend('0')
                else:
                    d[i].extend('1')
    print(d,'d')
    sav = sort_table(d,(availctr[0],availctr[1],availctr[2]))
    print(sav,'sav1')
    ranked_avail_data = []
    for i in range(len(sav)):
        ranked_avail_data.append(sav[i][1])
    print(ranked_avail_data,'ranked_avail_data')

    if len(workshop_lead) < 2:
        workshop_lead_list = ranked_avail_data
        for i in ranked_avail_data:
            if (WorkshopsTakenCount.objects.filter(name = i))[0].total_count < tcntt:
                index = workshop_lead_list.index(i)
                workshop_lead_list.pop(index)
        for i in workshop_lead_list:
            if len(workshop_lead) < 3:
                workshop_lead.append(i)
                msg = msg + ' ' + i + '(Lead)'
        print(workshop_lead,'workshop_lead')
        for i in workshop_lead:
            if i in ranked_avail_data:
                ranked_avail_data.remove(i)
        print(ranked_avail_data,'ranked_avail_data')

    if len(ranked_data) < 3:
        for i in ranked_avail_data:
            if len(ranked_data) < 3:
                 ranked_data.append(i)
                 msg = msg + ' ' + i + '(Member)'
        print(ranked_data,'ranked_data')

    return workshop_lead,ranked_data,msg

@api_view(['POST'])
def algo_for_willing_mem(request):
    var = JSONParser().parse(request)
    lang = var.get('lang')
    selectedworkshop = var.get('selectedworkshop')
    if len(selectedworkshop) < 1:
        return JsonResponse({'workshop_team':'please input workshop'})

    willcriteria = var.get('willcriteria')
    availcriteria = var.get('availcriteria')
    print(willcriteria,'willcriteria')
    willctr = []
    demo = int(var.get('demo'))
    tcnt = int(var.get('tcnt'))
    tcntt = int(var.get('tcntt'))
    for i in willcriteria:
        if i == 'Count of Willingness in Past Running Year':
            willctr.append(2)
        elif i == 'Highest Count of Workshop in Past Running Year':
            willctr.append(0)
        elif i == 'Linguistics Criteria':
            willctr.append(4)
        elif i == 'Count of Total Workshop':
            willctr.append(3)
    print(willctr)
    #step 1
    x = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop)
    mem_available = []
    for i in range(x.count()):
        if x[i].eYRC == '1':
            if x[i].approval_eYRC == 'None' or x[i].approval_eYRC == 'no':
                mem_available.append(x[i].responder )
        if x[i].eYIC == '1':
            if x[i].approval_eYIC == 'None' or x[i].approval_eYIC == 'no':
                mem_available.append(x[i].responder)
        if x[i].eYRDC == '1':
            if x[i].approval_eYRDC == 'None' or x[i].approval_eYRDC == 'no':
                mem_available.append(x[i].responder)
        if x[i].eLSI == '1':
            if x[i].approval_eLSI == 'None' or x[i].approval_eLSI == 'no':
                mem_available.append(x[i].responder)
        if x[i].web == '1':
            if x[i].approval_web == 'None' or x[i].approval_web == 'no':
                mem_available.append(x[i].responder)
        if x[i].course_or_other_eyantra_work == '1':
            if x[i].approval_course_or_other_eyantra_work == 'None' or x[i].approval_course_or_other_eyantra_work == 'no':
                mem_available.append(x[i].responder)
        if x[i].personal_or_any_other == '1':
            if x[i].approval_personal_or_any_other == 'None' or x[i].approval_personal_or_any_other == 'no':
                mem_available.append(x[i].responder)
    spl_mem_available = []
    [spl_mem_available.append(x) for x in mem_available if x not in spl_mem_available]
    print(spl_mem_available,'step1')
    #step 2
    y = WorkshopTeamStatus.objects.filter(workshop_id = 2 ,willingness_or_unavailability = 'Willingness')
    will_mem_available = []
    for i in range(y.count()):
        will_mem_available.append(y[i].responder)
    print(will_mem_available,'step2')
    #step 3
    z = DemoDtls.objects.all()
    for i in range(z.count()):
        if z[i].total_count_demo < demo:
            if z[i].name in will_mem_available:
                index = will_mem_available.index(z[i].name)
                will_mem_available.pop(index)
    print(will_mem_available,'step3')
    #step 4
    p = WorkshopsTakenCount.objects.all()
    d=[]
    def sort_table(table, cols):
        for col in reversed(cols):
            table = sorted(table, key=operator.itemgetter(col), reverse=True)
        return table
    for i in range(p.count()):
        for j in range(len(will_mem_available)):
            if will_mem_available[j] == p[i].name:
                d.append([p[i].past_year, p[i].name, p[i].willingness_shown,p[i].total_count])
    for i in range(len(d)):
        lang_data = userdetail.objects.filter(name = d[i][1])
        if lang_data[0].language is None:
            d[i].extend('0')
        else:
            l = lang_data[0].language.split(',')
            for j in l :
                print(j)
                if j == lang:
                    d[i].extend('1')
                else:
                    d[i].extend('0')
    print(d,'d')

    sav = sort_table(d,(willctr[0],willctr[1],willctr[2],willctr[3]))
    print(sav,'sav1')
    ranked_data = []
    for i in range(len(sav)):
        ranked_data.append(sav[i][1])
    print(ranked_data,'ranked_data')
    willing_team_lead = []
    for i in ranked_data:
        if (WorkshopsTakenCount.objects.filter(name = i))[0].total_count <= tcnt:
            willing_team_lead.append(i)
    print(willing_team_lead,'willing_team_lead')
    #step 10
    workshop_lead = willing_team_lead[0:2]
    print(workshop_lead,'workshop_lead')
    #step 11
    for i in workshop_lead:
        ranked_data.remove(i)
    print(ranked_data,'ranked_data')
    #step 12
    workshop_team  = []
    if len(workshop_lead) < 2 or len(ranked_data) < 3:
        workshop_lead,ranked_data,msg = algo_for_available_mem(spl_mem_available,workshop_lead,ranked_data,availcriteria,lang,tcntt)
        workshop_team = workshop_lead + ranked_data[:3]
        print(workshop_team,'workshop_team')
        print(msg)
        return JsonResponse({'workshop_team':workshop_team,'msg':msg})
    else:
        workshop_team = workshop_lead + ranked_data[:3]
        print(workshop_team,'workshop_team')
    # if len(will_mem_available) < 5:
        return JsonResponse({'workshop_team':workshop_team})



@api_view(['POST'])
def mailids(request):
    objs = userdetail.objects.all()
    print(objs)
    l = []
    for idx in range(objs.count()):
        l.append({'mailid':objs[idx].emailid,'name':objs[idx].name})
    #print(l)
    return JsonResponse({'data':l})

def form(request,uid,wid):
    return render(request,'form.html',context={'uuid':uid,'wid':wid})

def headapproval(request,uid,wid):
    headdet = headdetail.objects.filter(id = uid)
    wrkshp = create_workshop.objects.filter(id = wid)
    if headdet[0].head == 'eYRC':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,eYRC = '1')
    elif headdet[0].head == 'eYIC':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,eYIC = '1')
    elif headdet[0].head == 'eYRDC':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,eYRDC = '1')
    elif headdet[0].head == 'eLSI':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,eLSI = '1')
    elif headdet[0].head == 'web':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,web = '1')
    elif headdet[0].head == 'course_or_other_eyantra_work':
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,course_or_other_eyantra_work = '1')
    else:
        data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,personal_or_any_other = '1')
    return render(request,'headapproval.html',context={'uuid':uid,'wid':wid,'datas':data})

@api_view(['POST'])
def headresults(request):
    var = JSONParser().parse(request)
    print(var.get('uuid'),var.get('wid'),var.get('values'),var.get('names'))
    values = var.get('values')
    nms = var.get('names')
    wrkshp = create_workshop.objects.filter(id = var.get('wid'))
    headdet = headdetail.objects.filter(id = var.get('uuid'))
    '''
    eYRC,eYIC,eYRDC,eLSI,web,Course/Other e-Yantra Work,Personal/Any Other
    '''
    for idx in range(len(nms)):
        obj = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,
                responder = nms[idx])
        if headdet[0].head == 'eYRC':
            obj.update(approval_eYRC = values[idx])
        elif headdet[0].head == 'eYIC':
            obj.update(approval_eYIC = values[idx])
        elif headdet[0].head == 'eYRDC':
            obj.update(approval_eYRDC = values[idx])
        elif headdet[0].head == 'eLSI':
            obj.update(approval_eLSI = values[idx])
        elif headdet[0].head == 'web':
            obj.update(approval_web = values[idx])
        elif headdet[0].head == 'course_or_other_eyantra_work':
            obj.update(approval_course_or_other_eyantra_work = values[idx])
        elif headdet[0].head == 'personal_or_any_other':
            obj.update(approval_personal_or_any_other = values[idx])
    return Response('success')

@api_view(['POST'])
def formdata(request):
    var = JSONParser().parse(request)
    print(var.get('uuid'),var.get('wid'))
    wrkshp = create_workshop.objects.filter(id = var.get('wid'))
    category = var.get('category')
    feedreason = ['0','0','0','0','0','0','0']
    cat = ['eYRC','eYIC','eYRDC','eLSI','web','course_or_other_eyantra_work','personal_or_any_other']
    for i in range(len(category)):
        index = cat.index(category[i])
        feedreason[index] = '1'
    name = userdetail.objects.filter(id = var.get('uuid'))[0].name
    WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,
        responder = name).update(willingness_or_unavailability = var.get('option'),
        reason = var.get('reason'),eYRC = feedreason[0],eYIC = feedreason[1],
        eYRDC = feedreason[2],eLSI = feedreason[3],web = feedreason[4],
        course_or_other_eyantra_work = feedreason[5],
        personal_or_any_other = feedreason[6])
    return Response('success')

@api_view(['POST'])
def sendmail(request):
    var = JSONParser().parse(request)
    selectedworkshop = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = selectedworkshop)
    d = ElsiCollegeDtls.objects.filter(college_name = selectedworkshop)
    district = d[0].district
    #selected = var.get('selected')
    #print(selected)
    objs = userdetail.objects.all()
    d = {'sent':[],'success':'','failure':'','total':objs.count()}
    sucs = flr = 0
    for idx in range(objs.count()):
            dte = wrkshp[0].startdate + ' & ' + wrkshp[0].enddate
            serializer = WorkshopTeamSerializer(data = {'workshop_venue' : selectedworkshop,
                'date' : dte,'district' : district,'responder' : objs[idx].name})
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            to = objs[idx].emailid
            #if to in selected:
            uuid = objs[idx].id
            cc = ''
            bcc = ''
            subject = 'Workshop Team Selection Form'
            body = render_to_string(os.path.join(SCRIPTS_DIR,'link.html'),
                {'uid':uuid,'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
                'venue_address':wrkshp[0].venueadd,'start_date':wrkshp[0].startdate,
                'end_date':wrkshp[0].enddate})
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body)
            sent = True
            if sent:
                sucs+=1
                #d['sent'].append(to)
            else:
                flr+=1
    d['success'] = sucs
    d['failure'] = flr
    return JsonResponse(d)

@api_view(['POST'])
def headmail(request):
    var = JSONParser().parse(request)
    selectedworkshop = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = selectedworkshop)
    objs = headdetail.objects.all()
    d = {'sent':[],'success':'','failure':'','total':objs.count()}
    sucs = flr = 0
    #eYRC,eYIC,eYRDC,eLSI,web,Course/Other e-Yantra Work,Personal/Any Other
    rsnd = [{'eYRC':[]},{'eYIC':[]},{'eYRDC':[]},{'eLSI':[]},{'web':[]},
        {'course_or_other_eyantra_work':[]},{'personal_or_any_other':[]}]
    team = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop)
    for idx in range(team.count()):
        if team[idx].eYRC == '1':
            rsnd[0]['eYRC'].append(team[idx].responder)
        if team[idx].eYIC == '1':
            rsnd[1]['eYIC'].append(team[idx].responder)
        if team[idx].eYRDC == '1':
            rsnd[2]['eYRDC'].append(team[idx].responder)
        if team[idx].eLSI == '1':
            rsnd[3]['eLSI'].append(team[idx].responder)
            print(rsnd[3],'hii')
        if team[idx].web == '1':
            rsnd[4]['web'].append(team[idx].responder)
        if team[idx].course_or_other_eyantra_work == '1':
            rsnd[5]['course_or_other_eyantra_work'].append(team[idx].responder)
        if team[idx].personal_or_any_other == '1':
            rsnd[6]['personal_or_any_other'].append(team[idx].responder)
    print(rsnd)
    print(objs.count())
    for idx in range(objs.count()):
        to = objs[idx].emailid
        print(len(list(rsnd[idx].values())[0]))
        if len(list(rsnd[idx].values())[0]):
            uuid = objs[idx].id
            print(uuid)
            cc = ''
            bcc = ''
            subject = 'Workshop Team Selection approval'
            body = render_to_string(os.path.join(SCRIPTS_DIR,'headlink.html'),
                {'uid':uuid,'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
                'venue_address':wrkshp[0].venueadd,'start_date':wrkshp[0].startdate,
                'end_date':wrkshp[0].enddate})
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body)
            #sent = True
            if sent:
                sucs+=1
                d['sent'].append(to)
            else:
                flr+=1
    d['success'] = sucs
    d['failure'] = flr
    return JsonResponse(d)

######################
@api_view(['POST'])
def gethcn(request):
    var = JSONParser().parse(request)
    state=getname(str(var.get('state')))
    getdet = ElsiCollegeDtls.objects.filter(state = state).order_by('college_name')
    hcn = {}
    for i in range(getdet.count()):
        if "host" in hcn:
            hcn["host"].append(getdet[i].college_name)
        else:
            hcn["host"] = [getdet[i].college_name]
    print(hcn)
    return JsonResponse(hcn)
