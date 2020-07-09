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
from datetime import datetime,date,timedelta
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
from app.settings import EMAIL_HOST_USER,BASE_DIR,STATIC_DIR,ASSETS_DIR,TEMP_FILES_DIR
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from oauth2client.client import AccessTokenCredentials
import codecs
import os
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import urllib.parse
from time import sleep
import re
import platform
from pathlib import Path

#############################################################################################################
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
#
#
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
    #client_class = OAuth2Client

def get_user_info(credentials):
  """Send a request to the UserInfo API to retrieve the user's information.

  Args:
    credentials: oauth2client.client.OAuth2Credentials instance to authorize the
                 request.
  Returns:
    User information as a dict.
  """
  access_token = credentials['access_token']
  # url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={0}'.format(access_token)
  # r = requests.get(url)
  # data = r.json()
  # print(data,'data')
  credentials = AccessTokenCredentials(access_token, "MyAgent/1.0", None)
  print(credentials)
  file_path = os.path.join(ASSETS_DIR,'pickle.token')
  with open(file_path, 'wb') as token:
      pickle.dump(credentials, token)
  # if os.path.exists(file_path):
  #   with open(file_path, 'rb') as token:
  #       creds = pickle.load(token)
  #       print(creds,'1')
          # If there are no (valid) credentials available, let the user log in.
  # if not creds:
  #       if creds and creds.expired and creds.refresh_token:
  #           creds.refresh(Request())
  #       else:
  #           flow = InstalledAppFlow.from_client_secrets_file(
  #           credentials_path, SCOPES)
  #           creds = flow.run_local_server(host='127.0.0.1',port=8081)
            # Save the credentials for the next run
  #
  # user_info_service = build('oauth2', 'v2', credentials=credentials)
  # user_info = None
  # try:
  #   user_info = user_info_service.userinfo().get().execute()
  # except errors.HttpError:
  #   logging.error('An error occurred: %s', errors.HttpError)
  # if user_info and user_info.get('id'):
  #   return user_info
  # else:
  return 'done'

def check(credentials):
     access_token = credentials['access_token']
     url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={0}'.format(access_token)
     r = requests.get(url)
     data = r.json()
     print(data,'data')
     return data['email_verified']


@csrf_exempt
def gauthlogin(request):
    var = JSONParser().parse(request)
    toke = var.get('token')
    print(toke)
    # x = get_user_info(toke)
    # print(x)
    s = check(toke)
    if s:
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})
    # letshope = get_user_info(toke)
    # print(letshope)
    # if

@csrf_exempt
def authlogin(request):
    """Authenticates the user trying to login.

    Args:
        username(Json-obj): The login credential username.
        password(Json-obj): The login credential password.

    Returns:
        JsonResponse returning the status of login.
    """
    var = JSONParser().parse(request)
    name = var.get('username')
    passw = var.get('password')
    #print(User.objects.all().values())
    #print(User.objects.filter(logged_in='True').values())
    # logout required for login
    print(name,passw)
    if request.user.is_authenticated:
        return JsonResponse({'status':'already logged in'})
    # if form filled
    if request.method == 'POST':
        print('1here')
        user = authenticate(username=name, password=passw)
        print(user)
        if user is not None:
            print('1')
            if user.is_active:
                print('2')
                login(request, user)
                #print(User.objects.filter(logged_in = 'True').values())
                return JsonResponse({'status':'success'})

            else:
                print('3')
                return JsonResponse({'status':'Account Terminated!'})

        else:
            print('4')
            return JsonResponse({'status':'User Doesnt exist!'})

    # if new form is to be rendered
    else:
        print('5')
    return JsonResponse({'status':'Check method'})

@csrf_exempt
def authlogout(request):
    """logout the current logged in user.

    Returns:
        JsonResponse containing the status.
    """
    logout(request)
    #print(User.objects.filter(logged_in = 'True').values())
    return JsonResponse({'status':'logged out'})

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
def download(request):
    """Searches for message within gmail and downloads the attachments accordingly.

    Args:
        messageid(Json-obj): message id of the mail(message).

    Returns:
        JsonResponse returning either status of successfull download or error if any.
    """
    try:
        var = JSONParser().parse(request)
        mid = var.get('messageid')
        credentials = get_credentials()
        service = build('gmail', 'v1', credentials=credentials)
        msg = service.users().messages().get(userId='me', id=mid,format = 'full').execute()
        tmp = msg.get("payload").get("headers")
        downloads_path = str(Path.home() / "Downloads")
        print(downloads_path)
        attachments = []
        for idx in range(len(tmp)):
            if tmp[idx]['name'] == 'Subject' or  tmp[idx]['name'] == 'subject':
                subject = tmp[idx]['value']
        for part in msg['payload'].get('parts'):
            if part['filename']:
                file_name = part['filename']
                idx = file_name.rindex(".")
                now = str(datetime.now())[:19]
                now = now.replace(":","_")
                file_name = file_name[:idx]+"_"+str(now)+file_name[idx:]
                attachments.append(file_name)
                if 'data' in part['body']:
                    data=part['body']['data']
                else:
                    att_id=part['body']['attachmentId']
                    att=service.users().messages().attachments().get(userId='me', messageId=mid,id=att_id).execute()
                    data=att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                path = os.path.join(downloads_path,file_name)
                with open(path, 'wb') as f:
                    f.write(file_data)
        print(attachments)
        return JsonResponse({'status':'downloaded'})
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return JsonResponse({'status':error})

@api_view(['POST'])
def getmdtl(request):
    """Searches for message within gmail and gather details like subject, body and attachments.

    Args:
        messageid: message id of the mail.
        type: under sent, draft or inbox type.
    Returns:
        JsonResponse returning either subject, body and attachments of the message or error any any.
    """
    try:
        var = JSONParser().parse(request)
        mid = var.get('messageid')
        credentials = get_credentials()
        service = build('gmail', 'v1', credentials=credentials)
        msg = service.users().messages().get(userId='me', id=mid,format = 'full').execute()
        #print(msg)
        tmp = msg.get("payload").get("headers")
        attachments = []
        for idx in range(len(tmp)):
            if tmp[idx]['name'] == 'Subject' or  tmp[idx]['name'] == 'subject':
                subject = tmp[idx]['value']
        for part in msg['payload'].get('parts'):
            if part['filename']:
                attachments.append(part['filename'])
            else :
                if var.get('type') == 'inbox':
                    pass
                else:
                    pass
        if var.get('type') == 'inbox' :
            body = msg.get("payload").get("parts")[1].get('body')
            if body.get('attachmentId'):
                body = msg.get("payload").get("parts")[0].get('parts')[1].get('body')
        else :
            body = msg.get("payload").get("parts")[0].get('body')
            if not body['size']:
                body = msg.get("payload").get("parts")[0].get('parts')[0].get('parts')[0].get('body')
        bodydata = base64.urlsafe_b64decode(body.get("data").encode("ASCII")).decode("utf-8")
        return JsonResponse({'subject':subject,'body':bodydata,'attachments':attachments})
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return JsonResponse({'status':error})

@api_view(['POST'])
def stats(request):
    """This function is used to return the statistical data to Email Analytics page.

    Returns:
        JsonResponse containing the data about which user send the mails to whom about what(label), saved drafts and inbox responses.
    """
    try:
        obj = ssn_detail.objects.all()
        dct = {'Sent':[],'Inbox':[],'Draft':[]}
        lbl = []
        for idx in range(obj.count()):
            lst = obj[idx].mail_label.split(',')
            if 'DRAFT' in lst or not len(lst):
                for i in range(len(dct['Draft'])):
                    if dct['Draft'][i]['user'] == obj[idx].user:
                        if len(lst):
                            dct['Draft'][i]['Data']['count']+=1
                            dct['Draft'][i]['Data']['clist'].append((obj[idx].rcptmailid,obj[idx].messageid))
                        else:
                            dct['Draft'][i]['Data']['failed']+=1
                            dct['Draft'][i]['Data']['flist'].append((obj[idx].rcptmailid,obj[idx].messageid))
                        break
                else:
                    if len(lst):
                        dct['Draft'].append({'user':obj[idx].user,'Data':{'count':1,'failed':0,'clist':[(obj[idx].rcptmailid,obj[idx].messageid)],'flist':[]}})
                    else:
                        dct['Draft'].append({'user':obj[idx].user,'Data':{'count':0,'failed':1,'clist':[],'flist':[(obj[idx].rcptmailid,obj[idx].messageid)]}})
            else:
                for i in range(len(dct['Sent'])):
                    if dct['Sent'][i]['user'] == obj[idx].user:
                        break
                else:
                    i = len(dct['Sent'])
                    dct['Sent'].append({'user':obj[idx].user,'Data':[]})
                for j in range(len(dct['Sent'][i]['Data'])):
                    if dct['Sent'][i]['Data'][j]['label'] in lst:
                        if len(lst) == 1:
                            dct['Sent'][i]['Data'][j]['failed'] +=1
                            dct['Sent'][i]['Data'][j]['flist'].append((obj[idx].rcptmailid,obj[idx].messageid))
                        else :
                            dct['Sent'][i]['Data'][j]['count'] +=1
                            dct['Sent'][i]['Data'][j]['clist'].append((obj[idx].rcptmailid,obj[idx].messageid))
                        break
                else:
                    if len(lst) == 1:
                        lbl.append(lst[0])
                        dct['Sent'][i]['Data'].append({'label':lst[0],'count':0,'failed':1,'clist':[],'flist':[(obj[idx].rcptmailid,obj[idx].messageid)]})
                    else :
                        lbl.append(lst[1])
                        dct['Sent'][i]['Data'].append({'label':lst[1],'count':1,'failed':0,'clist':[(obj[idx].rcptmailid,obj[idx].messageid)],'flist':[]})
        print(dct)
        lbl = list(set(lbl))
        print(lbl)
        ids = []
        credentials = get_credentials()
        print(credentials,'credentials')
        service = build('gmail', 'v1', credentials=credentials)
        labels = ListLabels(service,'me')
        for val in labels:
            if val['name'] in lbl:
                ids.append(val['id'])
        msg = ListMessagesWithLabels(service,'me',['INBOX'])
        #print(msg)
        for idx in range(len(ids)):
            m = ListMessagesWithLabels(service,'me',[ids[idx]])
            for i in range(len(m)):
                for j in range(len(msg)):
                    if m[i]['threadId'] == msg[j]['threadId']:
                        tmp = service.users().messages().get(userId='me', id=msg[j]['id']).execute()
                        #print(tmp)
                        f = None;t = None
                        for l in range(len(tmp['payload']['headers'])):
                            if tmp['payload']['headers'][l]['name'] == 'From':
                                print(lbl[idx],tmp['payload']['headers'][l]['value'])
                                f = tmp['payload']['headers'][l]['value']
                                if f.find('<') != -1:
                                    f = f[f.index('<')+1:f.index('>')]
                            if tmp['payload']['headers'][l]['name'] == 'To':
                                print(lbl[idx],tmp['payload']['headers'][l]['value'])
                                t = tmp['payload']['headers'][l]['value']
                                if t.find('<') != -1:
                                    t = t[t.index('<')+1:t.index('>')]
                                break
                        if f and t :
                            for a in range(len(dct['Inbox'])):
                                if dct['Inbox'][a]['user'] == t:
                                    break
                            else:
                                a = len(dct['Inbox'])
                                dct['Inbox'].append({'user':t,'Data':[]})
                            for b in range(len(dct['Inbox'][a]['Data'])):
                                if dct['Inbox'][a]['Data'][b]['label'] == lbl[idx]:
                                    dct['Inbox'][a]['Data'][b]['count'] +=1
                                    dct['Inbox'][a]['Data'][b]['clist'].append((f,tmp['id']))
                                    break
                            else:
                                dct['Inbox'][a]['Data'].append({'label':lbl[idx],'count':1,'clist':[(f,tmp['id'])]})
        print(dct)
        return JsonResponse(dct)
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return JsonResponse({'status':error})    

def ListMessagesWithLabels(service, user_id, label_ids=[]):
  """List all Messages of the user's mailbox with label_ids applied.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print('An error occurred: %s' % error)
'''
@api_view(['POST'])
def getfile(request):
    print('hii')
    var = JSONParser().parse(request)
    v = var.get('value')
    if v == 'Pamphlet2020.pdf':
        with open(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path('Pamphlet2020.pdf'))
            return response
    else:
        with open(os.path.join(ASSETS_DIR,'letter-of-intent.docx'), 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path('letter-of-intent.docx'))
            return response
'''
def getbody(clg,obj,sta,dis):
        """ Creates the subject, body for send information mail part.

        Args:
            clg: It contains the given college name.
            obj: It contains the given college name details.
            sta: It contains the state of the college.
            dis: It contains the district of the college.

        Returns:
            subject: the subject content that is to be sent.
            body: the body content that is to be sent.
            subdiv: denotes the type of body content.
            tchdtl: contains the teacher details of the given college.
        """
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
                body = render_to_string(os.path.join(STATIC_DIR,'no_record.html'),{'count':count})
            else :
                college_name = obj[0].normalised_ins_name
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
                    body = render_to_string(os.path.join(STATIC_DIR,'elsi_college.html'),
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
                        body = render_to_string(os.path.join(STATIC_DIR,'tbt_complete.html'),
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
                        body = render_to_string(os.path.join(STATIC_DIR,'tbt_notcomplete.html'),
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
                    body = render_to_string(os.path.join(STATIC_DIR,'workshop_done.html'),
                    {'CollegeName':college_name,'State': state,'District':district,
                        'count':count,'host_college':temp[0].college_name,'host_State':temp[0].state,'host_District':temp[0].district,
                        "datas":d,'lst':l})
                else :
                    print('A')
                    subdiv = 'A'
                    body = render_to_string(os.path.join(STATIC_DIR,'no_record.html'),{'count':count})
            return {'subject':subject,'body':body,'subdiv':subdiv,'tchdtl':tchdtl}
        except ValueError as e:
            return {'status':'failed','info':e.args[0]}

def CreateLabel(service, user_id, label_object):
  """Creates a new label within user's mailbox, also prints Label ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_object: label to be added.

  Returns:
    Created Label.
  """
  try:
    label = service.users().labels().create(userId=user_id,
                                            body=label_object).execute()
    print(label['id'])
    return label
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def MakeLabel(label_name, mlv='show', llv='labelShow'):
  """Create Label object.

  Args:
    label_name: The name of the Label.
    mlv: Message list visibility, show/hide.
    llv: Label list visibility, labelShow/labelHide.

  Returns:
    Created Label.
  """
  label = {'messageListVisibility': mlv,
           'name': label_name,
           'labelListVisibility': llv}
  return label

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

def ListLabels(service, user_id):
  """Get a list all labels in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list all Labels in the user's mailbox.
  """
  try:
    response = service.users().labels().list(userId=user_id).execute()
    labels = response['labels']
    #for label in labels:
    #  print('Label id: %s - Label name: %s' % (label['id'], label['name']))
    return labels
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def SendMessage(sender, to, cc, bcc, subject, body,label,attachmentFile=None):
    
    credentials = get_credentials()
    print(credentials,'credentials')
    service = build('gmail', 'v1', credentials=credentials)
    #msgPlain = body
    #with open('templates/new.html' ,'r') as email_content:
        #msgHtml = email_content.read()
    labels = ListLabels(service,"me")
    for lbl in labels:
        if label == lbl['name']:
            label = lbl
            break
    else:
        label_obj = MakeLabel(label)
        print(label_obj)
        label = CreateLabel(service,"me",label_obj)
        print(label)
    if attachmentFile:
        message = createMessageWithAttachment(sender, to,cc,bcc, subject,body, attachmentFile)
    else:
        message = CreateMessageHtml(sender, to, cc, bcc, subject, body)
    result = SendMessageInternal(service, "me", message,label)
    return result

def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    file_path = os.path.join(ASSETS_DIR,'pickle.token')
    credentials_path=os.path.join(ASSETS_DIR,'credentials.json')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as token:
            creds = pickle.load(token)
            #print(creds,'1')
        # If there are no (valid) credentials available, let the user log in.
    if not creds:
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

def SendMessageInternal(service, user_id, message,label):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        msg_labels = {'removeLabelIds': [], 'addLabelIds': label['id']}
        message = service.users().messages().modify(userId=user_id,id=message['id'],body=msg_labels).execute()
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
    print(message)
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
    # API_KEY = 'AIzaSyD9qTJmiFUe3FQWlo5Z-A3l6pigxA3s8U8'
    # url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    # input=name
    # input.replace(" ", "%")
    # other='&inputtype=textquery&fields=name'
    # result = requests.get(url+'input='+input+other+'&key='+API_KEY)
    # collx = result.json()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--silent")
    options.add_argument('--ignore-certificate-errors')
    if platform.system() == 'Windows':
        file_path = os.path.join(ASSETS_DIR,'chromedriver.exe')
    else :
        file_path = os.path.join(ASSETS_DIR,'chromedriver')
    driver = webdriver.Chrome(executable_path=file_path, options=options) #path to chromedriver.exe
    def test(name):
        q1= urllib.parse.quote(name)
        driver.get('https://www.google.com/search?q=' + q1)#add college name to be searched in query
        html= driver.page_source
        soup = BeautifulSoup(html,"html.parser")
        if soup.find('div', attrs={'data-attrid':'title'}) :
            name = soup.find('div', attrs={'data-attrid':'title'}).span.contents
            return name
        else:
            return "no data"
    coll = test(name)
    driver.quit()
    return coll[0]
    # if collx['status'] == 'REQUEST_DENIED':
    #     return name
    # else:
    #     return collx['candidates'][0]['name']
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
            # if len(district) >0 and len(state)>0:
            #     dis = getname(str(var.get('district')))
            #     sta = getname(str(var.get('state')))
            # else:
            #     collx = getloc(coll)
            #     data = collx['candidates'][0]['formatted_address']
            #     data.replace(" ", "")
            #     data = data.split(",")
            #     dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
            #     print(dis)
            #     sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
            #     print(sta)
            obj = ElsiCollegeDtls.objects.filter(normalised_ins_name = coll)
            c = ElsiCollegeDtls.objects.all()
            count=0
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            if obj.count() < 1:
                pass
            else :
                college_name = obj[0].normalised_ins_name
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
                    body = render_to_string(os.path.join(STATIC_DIR,'elsi_college.html'),
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
                        body = render_to_string(os.path.join(STATIC_DIR,'tbt_complete.html'),
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
                        body = render_to_string(os.path.join(STATIC_DIR,'tbt_notcomplete.html'),
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
                    body = render_to_string(os.path.join(STATIC_DIR,'workshop_done.html'),
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
    user = request.data.get('user')
    label = request.data.get('label')
    with open('assets/info.json','r') as read:
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
                clg = row[6]
                coll = getname(clg)
                obj = ElsiCollegeDtls.objects.filter(normalised_ins_name = coll)
                print(coll)
                fn = []
                # if len(district) >0 and len(state)>0:
                #     dis = getname(district)
                #     sta = getname(state)
                # else:
                #     data = collx['candidates'][0]['formatted_address']
                #     data.replace(" ", "")
                #     data = data.split(",")
                #     dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                #     print(dis)
                #     sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                #     print(sta)
                res = getbody(coll,obj,state,district)
                subject = res['subject']
                body = res['body']
                files2send2 = list(request.data.get('file2send2').split(","))
                print(files2send2)
                attachments = []
                for f in files2send2:
                    if f == 'Pamphlet2020.pdf':
                        attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
                    elif f == 'letter-of-intent.docx':
                        attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
                if request.FILES :
                    for i in request.FILES:
                        file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
                        fn.append(file_name)
                        attachments.append(os.path.join(BASE_DIR,file_name))
                sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label,attachments)
                now = datetime.now()
                ts = now.strftime("%Y-%m-%d %H:%M:%S")
                if sent :
                    # res['msg'] = "mail sent successfully"
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("1")
                    else:
                      re["status"] = ["1"]
                    serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'SENT,'+label,'rcptmailid' : to,
                        'delegated_access':'1','dcprovider':'None','messageid':sent['id']})
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
                    serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : label,'rcptmailid' : to,
                        'delegated_access':'1','dcprovider':'None','messageid':'None'})
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
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
    user = request.data.get('user')
    with open('assets/info.json','r') as read:
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
                clg = row[6]
                coll = getname(clg)
                obj = ElsiCollegeDtls.objects.filter(normalised_ins_name = coll)
                print(coll)
                # if len(district) >0 and len(state)>0:
                #     dis=getname(district)
                #     sta = getname(state)
                # else:
                #     data = collx['candidates'][0]['formatted_address']
                #     data.replace(" ", "")
                #     data = data.split(",")
                #     dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
                #     print(dis)
                #     sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
                #     print(sta)
                res = getbody(coll,obj,state,district)
                subject = res['subject']
                body = res['body']
                files2send2 = list(request.data.get('file2send2').split(","))
                print(files2send2)
                attachments = []
                for f in files2send2:
                    if f == 'Pamphlet2020.pdf':
                        attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
                    elif f == 'letter-of-intent.docx':
                        attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
                fn = []
                if request.FILES :
                    for i in request.FILES:
                        file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
                        fn.append(file_name)
                        attachments.append(os.path.join(BASE_DIR,file_name))
                attachmentFile = attachments
                if attachmentFile:
                    message = createMessageWithAttachment(EMAIL_HOST_USER, to,cc,bcc, subject,body, attachmentFile)
                else:
                    message = CreateMessageHtml(EMAIL_HOST_USER, to, cc, bcc, subject, body)
                result = CreateDraft(service,"me",message)
                now = datetime.now()
                ts = now.strftime("%Y-%m-%d %H:%M:%S")
                if result :
                    # res['msg'] = "mail sent successfully"
                    if "to" in re:
                      re["to"].append(to)
                    else:
                      re["to"] = [to]
                    if "status" in re:
                      re["status"].append("1")
                    else:
                      re["status"] = ["1"]
                    serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                                    'timestamp' : ts,'mail_label' : 'DRAFT','rcptmailid' : to,
                                    'delegated_access':'0','dcprovider':'None','messageid':result['message']['id']})
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
                    serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                                    'timestamp' : ts,'mail_label' : '','rcptmailid' : to,
                                    'delegated_access':'0','dcprovider':'None','messageid':'None'})
                if serializer.is_valid():
                    serializer.save()
                else :
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
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
    # if len(district) >0 and len(state)>0:
    #     dis=getname(district)
    #     sta=getname(state)
    # else:
    #     collx = getloc(coll)
    #     data = collx['candidates'][0]['formatted_address']
    #     data.replace(" ", "")
    #     data = data.split(",")
    #     dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
    #     print(dis)
    #     sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
    #     print(sta)
    d = {'to' : rema  ,'cc' : cc,'bcc' : bcc,'subject': '','body':'','attachments':''}
    res = getbody(coll,obj,state,district)
    d['subject'] = res['subject']
    d['body'] = res['body']
    d['attachments'] = {'pamp':'Pamphlet2020.pdf','LoI':'letter-of-intent.docx'}
    d['attachmentlinks'] = {'pamp':'https://www.e-yantra.org/img/Pamphlet2020.pdf','LoI':'http://elsi.e-yantra.org/eyrtc/downloads/loi'}
    return JsonResponse(d)

@api_view(['POST'])
def csvsubmit(request):
    file = request.FILES['file']
    if os.path.getsize('assets/info.json') :
        with open('assets/info.json','r') as read:
            obj = json.load(read)
            if os.path.exists(obj['file_path']):
                os.remove(obj['file_name'])
    file_name = default_storage.save(file.name,file)
    CSV_DIR = os.path.join(BASE_DIR,file_name)
    with open('assets/info.json','w') as write :
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
            if '(' in district:
                district = re.sub(r'\([^)]*\)', '', district)[0:-1]
            print(district)
            state = var.get('state')
            if '(' in state:
                state = re.sub(r'\([^)]*\)', '', state)[0:-1]
            print(state)
            coll = getname(var.get('cname'))
            print(coll)
            # if len(district) >0 and len(state)>0:
            #     dis=getname(str(var.get('district')))
            #     sta=getname(str(var.get('state')))
            # else:
            #     collx = getloc(coll)
            #     data = collx['candidates'][0]['formatted_address']
            #     data.replace(" ", "")
            #     data = data.split(",")
            #     dis = "".join(filter(lambda x: not x.isdigit(), data[-3]))
            #     print(dis)
            #     sta = "".join(filter(lambda x: not x.isdigit(), data[-2]))
            #     print(sta)
            obj = ElsiCollegeDtls.objects.filter(normalised_ins_name = clg)
            res = getbody(coll,obj,state,district)
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
            user = request.data.get('user')
            if request.user.is_authenticated:
                print({'status':'already logged in'})
            to = request.data.get('remail')
            label = request.data.get('label')
            # if type(request.data.get('cc')) == list:
            #     cc = ','.join(map(str,request.data.get('cc') ))
            # else:
            cc = request.data.get('cc')
            # if type(request.data.get('bcc')) == list:
            #     bcc = ','.join(map(str,request.data.get('bcc') ))
            # else:
            bcc = request.data.get('bcc')
            subject = request.data.get('subject')
            body = request.data.get('body')
            sent = None
            files2send1 = list(request.data.get('files2send1').split(","))
            print(files2send1)
            attachments = []
            for f in files2send1:
                if f == 'Pamphlet2020.pdf':
                    attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
                elif f == 'letter-of-intent.docx':
                    attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
            fn = []
            if request.FILES :
                for i in request.FILES:
                    file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
                    fn.append(file_name)
                    attachments.append(os.path.join(BASE_DIR,file_name))
            print(attachments)
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label,attachments)
            now = datetime.now()
            ts = now.strftime("%Y-%m-%d %H:%M:%S")
            if 'file1' in request.FILES :
                os.remove(os.path.join(BASE_DIR,file_name))
            if sent :
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'SENT,'+label,'rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':sent['id']})
                if serializer.is_valid():
                    serializer.save()
                else :
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
                return JsonResponse({'status':'success','info':'mail sent successfully'})
            else :
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : label,'rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':'None'})
                if serializer.is_valid():
                    serializer.save()
                else :
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
                return JsonResponse({'status':'failure','info':'mail was not sent'})
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def gsave(request):
    to = request.data.get('remail')
    user = request.data.get('user')
    # if type(request.data.get('cc')) == list:
    #     cc = ','.join(map(str,request.data.get('cc') ))
    # else:
    cc = request.data.get('cc')
    # if type(request.data.get('bcc')) == list:
    #     bcc = ','.join(map(str,request.data.get('bcc') ))
    # else:
    bcc = request.data.get('bcc')
    subject = request.data.get('subject')
    body = request.data.get('body')
    sent = None
    files2send1 = list(request.data.get('files2send1').split(","))
    print(files2send1)
    attachments = []
    for f in files2send1:
        if f == 'Pamphlet2020.pdf':
            attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
        elif f == 'letter-of-intent.docx':
            attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
    fn = []
    if request.FILES :
        for i in request.FILES:
            file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
            fn.append(file_name)
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
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    if result:
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'DRAFT','rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':result['message']['id']})
    else:
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : '','rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':'None'})
    if serializer.is_valid():
        serializer.save()
    else :
        print(serializer.errors)
    print(serializer)
    for i in range(len(fn)):
        os.remove(os.path.join(BASE_DIR,fn[i]))
    return JsonResponse({'status':'saved to draft'})
######################

######################
#workshop announcement
@api_view(['POST'])
def cwssubmit(request):
        try:
            var = JSONParser().parse(request)
            x = var.get('coono')
            print(x)
            clgid = ElsiCollegeDtls.objects.filter(college_name = var.get('hcn'))[0].id
            serializer = CreateWorkshop(data={'clgid':clgid,'hcn':var.get('hcn'),'startdate':var.get('startdate'),
                'enddate':var.get('enddate'),'venueadd':var.get('venueadd'),'cooname':var.get('cooname'),
                'cooemail':var.get('cooemail'),'coono':var.get('coono')})
            #print(serializer.is_valid())
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
                    wrklist["list"].append((obj[i].hcn,obj[i].isactive))
                else:
                    wrklist["list"] = [(obj[i].hcn,obj[i].isactive)]
            print(wrklist)
            return JsonResponse(wrklist)
        except ValueError as e:
            return JsonResponse({'status':'failed','info':e.args[0]})

@api_view(['POST'])
def savewrkactv(request):
        try:
            var = JSONParser().parse(request)
            obj = create_workshop.objects.filter(hcn = var.get('workshop'))
            obj.update(isactive = var.get('isactive'))
            print(obj.values())
            return JsonResponse({'status':'saved'})
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
            if '(' in state:
                state = re.sub(r'\([^)]*\)', '', state)[0:-1]
            print(state)
            districts = var.get('district')
            c = ElsiCollegeDtls.objects.all()
            count=0
            for c in c.values('lab_inaugurated'):
                if c.get('lab_inaugurated') == 1:
                    count=count+1
            obj1 = AICTE_list.objects.filter(state__iexact = state)
            print(obj1)
            if obj1.count() >= 1:
                for district in districts:
                    if '(' in district:
                        district = re.sub(r'\([^)]*\)', '', district)[0:-1]
                    print(district)
                    obj2 = AICTE_list.objects.filter(district__iexact = district)
                    if obj2.count() >= 1:
                        for rows in list(obj2.values()) :
                            clist = clist + [(rows['email'])]
                if len(clist) == 0:
                    print(clist)
                    return JsonResponse({'key':'nodata'})
                else:
                    print(clist)
                    dict['bcc'] = clist
                    print(dict)
                    subject = "IIT Bombay, e-Yantra Lab Setup Initiative (eLSI): +\
                     Invitation to Attend the Two Day Workshop at " + hcn +", " + getdet[0].district +", " + getdet[0].state
                    body = render_to_string(os.path.join(STATIC_DIR,'announce_workshop.html'),
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
def awsapprove(request):
        try:
            #print(request.data.get('file1'))
            #print(request.data.get('file2'))
            user = request.data.get('user')
            if request.user.is_authenticated:
                print({'status':'already logged in'})
            to = request.data.get('remail')
            label = request.data.get('label')
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
                    attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
                elif f == 'letter-of-intent.docx':
                    attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
            fn = []
            if request.FILES :
                for i in request.FILES:
                    file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
                    fn.append(file_name)
                    attachments.append(os.path.join(BASE_DIR,file_name))
            print(attachments)
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label,attachments)
            now = datetime.now()
            ts = now.strftime("%Y-%m-%d %H:%M:%S")
            if 'file1' in request.FILES :
                os.remove(os.path.join(BASE_DIR,file_name))
            if sent :
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'SENT,'+label,'rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':sent['id']})
                if serializer.is_valid():
                    serializer.save()
                else :
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
                return JsonResponse({'status':'success','info':'mail sent successfully'})
            else :
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : label,'rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':'None'})
                if serializer.is_valid():
                    serializer.save()
                else :
                    print(serializer.errors)
                print(serializer)
                for i in range(len(fn)):
                    os.remove(os.path.join(BASE_DIR,fn[i]))
                return JsonResponse({'status':'failure','info':'mail was not sent'})
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def awsgsave(request):
    to = request.data.get('remail')
    user = request.data.get('user')
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
            attachments.append(os.path.join(ASSETS_DIR,'Pamphlet2020.pdf'))
        elif f == 'letter-of-intent.docx':
            attachments.append(os.path.join(ASSETS_DIR,'letter-of-intent.docx'))
    fn = []
    if request.FILES :
        for i in request.FILES:
            file_name = default_storage.save(request.FILES[i].name, request.FILES[i])
            fn.append(file_name)
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
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    if result:
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'DRAFT','rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':result['message']['id']})
    else:
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : '','rcptmailid' : to,
                        'delegated_access':'0','dcprovider':'None','messageid':'None'})
    if serializer.is_valid():
        serializer.save()
    else :
        print(serializer.errors)
    print(serializer)
    for i in range(len(fn)):
        os.remove(os.path.join(BASE_DIR,fn[i]))
    return JsonResponse({'status':'saved to draft'})


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
catlist = ['eYRC','eYIC','eYRDC','eLSI','web','course_or_other_eyantra_work','personal_or_any_other']
@api_view(['POST'])
def kavi_sir_mail(request):
    var = JSONParser().parse(request)
    user = var.get('user')
    selectedworkshop = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = selectedworkshop)
    d = ElsiCollegeDtls.objects.filter(college_name = selectedworkshop)
    label = var.get('label')
    tm = var.get('team')
    print(tm)
    team = []
    for idx in range(len(tm)):
        cnt = WorkshopsTakenCount.objects.filter(name = tm[idx])[0].total_count
        sts = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop,responder = tm[idx])[0].willingness_or_unavailability
        team.append({'name':tm[idx],'count':cnt,'status':sts})
    district = d[0].district
    state = d[0].state
    stat = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop)
    app = memberdetail.objects.all()
    dte = wrkshp[0].startdate + ' & ' + wrkshp[0].enddate
    d = {'sent':[],'success':'','failure':''}
    sucs = flr = 0
    start_date = wrkshp[0].startdate
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    start_date = datetime.strftime(start_date,'%B %d, %Y')
    end_date = wrkshp[0].enddate
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    end_date = datetime.strftime(end_date,'%B %d, %Y')
    to = '98dikshitajain@gmail.com'
    cc = ''
    bcc = ''
    subject = 'Workshop team for workshop at ' +  wrkshp[0].hcn + ' ,' + district + ' ,'+ state + ' on ' + start_date + ' - ' + end_date + '.'
    body = render_to_string(os.path.join(STATIC_DIR,'kavi_sir_mail.html'),
    {'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
    'venue_address':wrkshp[0].venueadd,'start_date':start_date,
    'end_date':end_date,'district': district,'state' : state,'dte':dte,'stat':stat,'team':team})
    sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label)
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    if sent:
        sucs+=1
        d['sent'].append(to)
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                    'timestamp' : ts,'mail_label' : 'SENT,'+label,'rcptmailid' : to,
                    'delegated_access':'1','dcprovider':'None','messageid':sent['id']})
    else:
        flr+=1
        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                    'timestamp' : ts,'mail_label' : label,'rcptmailid' : to,
                    'delegated_access':'1','dcprovider':'None','messageid':'None'})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        print(serializer)
    d['success'] = sucs
    d['failure'] = flr
    return JsonResponse(d)

@api_view(['POST'])
def getalgodetail(request):
    obj = algo_detail.objects.all()
    algodetail = {}
    algodetail['demo'] = obj[0].demo_module_cnt
    algodetail['tcnt'] = obj[0].will_ttl_wrkshp_cnt
    algodetail['tcntt'] = obj[0].aval_ttl_wrkshp_cnt
    algodetail['willcriteria'] = obj[0].willcriteria.split(',')
    algodetail['availcriteria'] = obj[0].availcriteria.split(',')
    print(algodetail)
    return JsonResponse(algodetail)

@api_view(['POST'])
def savealgo(request):
    var = JSONParser().parse(request)
    willcriteria = ','.join(var.get('willcriteria'))
    availcriteria = ','.join(var.get('availcriteria'))
    lang = var.get('lang')
    tcnt = var.get('tcnt')
    tcntt = var.get('tcntt')
    demo = var.get('demo')
    print(willcriteria)
    obj = algo_detail.objects.all()
    if obj.count() :
        obj.update(demo_module_cnt = demo,
            will_ttl_wrkshp_cnt = tcnt,
            aval_ttl_wrkshp_cnt = tcntt,
            willcriteria = willcriteria,
            availcriteria = availcriteria)
    else:
        serializer = AlgoDetailSerializer(data = {'demo_module_cnt': 4,'will_ttl_wrkshp_cnt' : 4,
                    'aval_ttl_wrkshp_cnt' : 4, 'willcriteria' : 'Count of Willingness in Past Running Year,Highest Count of Workshop in Past Running Year,Linguistics Criteria,Count of Total Workshop'
,'availcriteria' : 'Highest Count of Workshop in Past Running Year,Linguistics Criteria,Count of Total Workshop'})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        else :
            print(serializer.errors)
    print(obj.values())
    return JsonResponse({'status':'success'})

@api_view(['POST'])
def getlang(request):
    try:
        obj = memberdetail.objects.all()
        lang = {}
        for i in range(obj.count()):
            if obj[i].language:
                x = list((obj[i].language).split(','))
                for i in x:
                    if "list" in lang:
                        if i not in lang['list']:
                            lang["list"].append(i)
                    else:
                        lang["list"] = [i]
        print(lang)
        return JsonResponse(lang)
    except ValueError as e:
        return JsonResponse({'status':'failed','info':e.args[0]})

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
        lang_data = memberdetail.objects.filter(name = d[i][1])
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
    wid = create_workshop.objects.filter(hcn = selectedworkshop)[0].id
    print(selectedworkshop,wid)
    willcriteria = var.get('willcriteria')
    availcriteria = var.get('availcriteria')
    print(willcriteria,'willcriteria')
    willctr = []
    demo = int(var.get('demo'))
    tcnt = int(var.get('tcnt'))
    tcntt = int(var.get('tcntt'))
    print(tcntt)
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
    #print(x)
    mem_available = []
    for i in range(x.count()):
        if x[i].approval_status == 'None' or x[i].approval_status == 'no':
            mem_available.append(x[i].responder)
    spl_mem_available = []
    [spl_mem_available.append(x) for x in mem_available if x not in spl_mem_available]
    print(spl_mem_available,'step1')
    #step 2
    y = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop,willingness_or_unavailability = 'willingness')
    #print(y)
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
        lang_data = memberdetail.objects.filter(name = d[i][1])
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
        workshop_team = workshop_lead + ranked_data
        print(workshop_team,'workshop_team')
        print(msg)
        return JsonResponse({'workshop_team':workshop_team,'msg':msg})
    else:
        workshop_team = workshop_lead + ranked_data
        print(workshop_team,'workshop_team')
    # if len(will_mem_available) < 5:
        return JsonResponse({'workshop_team':workshop_team})


'''
@api_view(['POST'])
def mailids(request):
    objs = memberdetail.objects.filter(team = '1')
    print(objs)
    l = []
    for idx in range(objs.count()):
        l.append({'mailid':objs[idx].emailid,'name':objs[idx].name})
    #print(l)
    return JsonResponse({'data':l})
'''
def form(request,uid,wid):
    return render(request,'form.html',context={'uuid':uid,'wid':wid})

def headapproval(request,uid,wid):
    headdet = memberdetail.objects.filter(id = uid)
    wrkshp = create_workshop.objects.filter(id = wid)
    data = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,approved_or_rejected_by=headdet[0].name)
    return render(request,'headapproval.html',context={'uuid':uid,'wid':wid,'datas':data})

@api_view(['POST'])
def headresults(request):
    var = JSONParser().parse(request)
    print(var.get('uuid'),var.get('wid'),var.get('values'),var.get('names'))
    values = var.get('values')
    nms = var.get('names')
    wrkshp = create_workshop.objects.filter(id = var.get('wid'))
    headdet = memberdetail.objects.filter(id = var.get('uuid'))
    for idx in range(len(nms)):
        obj = WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,
                responder = nms[idx])
        obj.update(approval_status = values[idx])
    return Response('success')

@api_view(['POST'])
def formdata(request):
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    var = JSONParser().parse(request)
    print(var.get('uuid'),var.get('wid'),var.get('category'))
    wrkshp = create_workshop.objects.filter(id = var.get('wid'))
    name = memberdetail.objects.filter(id = var.get('uuid'),team = '1')[0].name
    WorkshopTeamStatus.objects.filter(workshop_venue = wrkshp[0].hcn,
        responder = name).update(timestamp = ts,willingness_or_unavailability = var.get('option'),
        reason = var.get('reason'),category_of_reason = var.get('category'))
    return Response('success')

@api_view(['POST'])
def sendmail(request):
    var = JSONParser().parse(request)
    user = var.get('user')
    selectedworkshop = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = selectedworkshop)
    d = ElsiCollegeDtls.objects.filter(college_name = selectedworkshop)
    label = var.get('label')
    district = d[0].district
    state = d[0].state
    today = date.today()
    last_date = today + timedelta(3)
    #last_date = datetime.strptime(last_date, '%d-%m-%Y')
    last_date = datetime.strftime(last_date,'%B %d, %Y')
    start_date = wrkshp[0].startdate
    #start_date = datetime.strptime(start_date, '%Y-%m-%d')
    start_date = datetime.strftime(start_date,'%B %d, %Y')
    end_date = wrkshp[0].enddate
    #end_date = datetime.strptime(end_date, '%Y-%m-%d')
    end_date = datetime.strftime(end_date,'%B %d, %Y')
    #selected = var.get('selected')
    #print(selected)
    objs = memberdetail.objects.filter(team = '1')
    d = {'sent':[],'success':'','failure':'','total':objs.count()}
    sucs = flr = 0
    for idx in range(objs.count()):
            dte = wrkshp[0].startdate + ' & ' + wrkshp[0].enddate
            serializer = WorkshopTeamSerializer(data = {'workshop_id':wrkshp[0].id,'workshop_venue' : selectedworkshop,
                'date' : dte,'district' : district,'responder' : objs[idx].name})
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else :
                print(serializer.errors)
            to = objs[idx].emailid
            #if to in selected:
            uuid = objs[idx].id
            cc = ''
            bcc = ''
            subject = 'Regarding Workshop Team for upcoming workshop at ' +  wrkshp[0].hcn + ' ,' + district + ' ,'+ state + ' .'
            body = render_to_string(os.path.join(STATIC_DIR,'link.html'),
                {'uid':uuid,'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
                'venue_address':wrkshp[0].venueadd,'start_date':start_date,
                'end_date':end_date,'district': district,'state' : state,'last_date':last_date})
            sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label)
            now = datetime.now()
            ts = now.strftime("%Y-%m-%d %H:%M:%S")
            if sent:
                sucs+=1
                d['sent'].append(to)
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : 'SENT,'+label,'rcptmailid' : to,
                        'delegated_access':'1','dcprovider':'None','messageid':sent['id']})
            else:
                flr+=1
                serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                        'timestamp' : ts,'mail_label' : label,'rcptmailid' : to,
                        'delegated_access':'1','dcprovider':'None','messageid':'None'})
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
            print(serializer)
    d['success'] = sucs
    d['failure'] = flr
    return JsonResponse(d)

@api_view(['POST'])
def headmail(request):
    var = JSONParser().parse(request)
    user = var.get('user')
    selectedworkshop = var.get('selectedworkshop')
    wrkshp = create_workshop.objects.filter(hcn = selectedworkshop)
    objs = memberdetail.objects.filter(ishead = '1')
    print(objs)
    label = var.get('label')
    d = {'sent':[],'success':'','failure':'','total':objs.count()}
    sucs = flr = 0
    start_date = wrkshp[0].startdate
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    start_date = datetime.strftime(start_date,'%B %d, %Y')
    end_date = wrkshp[0].enddate
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    end_date = datetime.strftime(end_date,'%B %d, %Y')
    #eYRC,eYIC,eYRDC,eLSI,web,Course/Other e-Yantra Work,Personal/Any Other
    rsnd = [{'eYRC':[]},{'eYIC':[]},{'eYRDC':[]},{'eLSI':[]},{'web':[]},
        {'course_or_other_eyantra_work':[]},{'personal_or_any_other':[]}]
    team = WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop)
    for idx in range(team.count()):
        if team[idx].category_of_reason and 'eYRC' in team[idx].category_of_reason :
            rsnd[0]['eYRC'].append(team[idx].responder)
        if team[idx].category_of_reason and 'eYIC' in team[idx].category_of_reason:
            rsnd[1]['eYIC'].append(team[idx].responder)
        if team[idx].category_of_reason and 'eYRDC' in team[idx].category_of_reason:
            rsnd[2]['eYRDC'].append(team[idx].responder)
        if team[idx].category_of_reason and 'eLSI' in team[idx].category_of_reason:
            rsnd[3]['eLSI'].append(team[idx].responder)
        if team[idx].category_of_reason and 'web' in team[idx].category_of_reason:
            rsnd[4]['web'].append(team[idx].responder)
        if team[idx].category_of_reason and 'course_or_other_eyantra_work' in team[idx].category_of_reason:
            rsnd[5]['course_or_other_eyantra_work'].append(team[idx].responder)
        if team[idx].category_of_reason and 'personal_or_any_other' in team[idx].category_of_reason:
            rsnd[6]['personal_or_any_other'].append(team[idx].responder)
    print(rsnd)
    print(objs.count())
    for idx in range(objs.count()):
        #print(len(list(rsnd[idx].values())[0]))
        for i in range(len(rsnd)):
            if objs[idx].head in list(rsnd[i].keys())[0] and len(list(rsnd[i].values())[0]):
                #print('1')
                if objs[idx].name in list(rsnd[i].values())[0]:
                    #print('2')
                    cohead = memberdetail.objects.filter(iscohead = '1',cohead = list(rsnd[i].keys())[0])
                    to = cohead[0].emailid
                    uuid = cohead[0].id
                    print(cohead[0].name)
                    WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop, responder = name).update(approved_or_rejected_by = cohead[0].name)
                    print(objs[idx].name)
                    cc = ''
                    bcc = ''
                    subject = 'Workshop Team Selection approval'
                    body = render_to_string(os.path.join(STATIC_DIR,'headlink.html'),
                        {'uid':uuid,'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
                        'venue_address':wrkshp[0].venueadd,'start_date':start_date,
                        'end_date':end_date,'responder_list':cohead[0].name})
                    sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label)
                    now = datetime.now()
                    ts = now.strftime("%Y-%m-%d %H:%M:%S")
                    if sent:
                        sucs+=1
                        d['sent'].append(to)
                        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                            'timestamp' : ts,'mail_label' : 'DRAFT','rcptmailid' : to,
                            'delegated_access':'1','dcprovider':'None','messageid':sent['id']})
                    else:
                        flr+=1
                        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                            'timestamp' : ts,'mail_label' : '','rcptmailid' : to,
                            'delegated_access':'1','dcprovider':'None','messageid':'None'})
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                    print(serializer)
                if  objs[idx].name in list(rsnd[i].values())[0] or len(list(rsnd[i].values())[0]) >= 1:
                    #print('3')
                    to = objs[idx].emailid
                    uuid = objs[idx].id
                    responder_list = []
                    for name in list(rsnd[i].values())[0]:
                        if name != objs[idx].name:
                            responder_list.append(name)
                            WorkshopTeamStatus.objects.filter(workshop_venue = selectedworkshop, responder = name).update(approved_or_rejected_by = objs[idx].name)
                    print(responder_list)
                    print(objs[idx].name)
                    cc = ''
                    bcc = ''
                    subject = 'Workshop Team Selection approval'
                    body = render_to_string(os.path.join(STATIC_DIR,'headlink.html'),
                        {'uid':uuid,'wid':wrkshp[0].id,'workshop_name':wrkshp[0].hcn,
                        'venue_address':wrkshp[0].venueadd,'start_date':start_date,
                        'end_date':end_date,'responder_list':responder_list})
                    sent  = SendMessage(EMAIL_HOST_USER,to,cc,bcc,subject,body,label)
                    now = datetime.now()
                    ts = now.strftime("%Y-%m-%d %H:%M:%S")
                    if sent:
                        sucs+=1
                        d['sent'].append(to)
                        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                            'timestamp' : ts,'mail_label' : 'DRAFT','rcptmailid' : to,
                            'delegated_access':'1','dcprovider':'None','messageid':sent['id']})
                    else:
                        flr+=1
                        serializer = SsnSerializer(data = {'ssn_id':'ssn1','user' : user,
                            'timestamp' : ts,'mail_label' : '','rcptmailid' : to,
                            'delegated_access':'1','dcprovider':'None','messageid':'None'})
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                    print(serializer)
    d['success'] = sucs
    d['failure'] = flr
    return JsonResponse(d)

######################
@api_view(['POST'])
def gethcn(request):
    var = JSONParser().parse(request)
    state=var.get('state')
    if '(' in state:
        state = re.sub(r'\([^)]*\)', '', state)[0:-1]
    print(state)
    getdet = ElsiCollegeDtls.objects.filter(state__iexact = state).order_by('college_name')
    hcn = {}
    for i in range(getdet.count()):
        if "host" in hcn:
            hcn["host"].append(getdet[i].college_name)
        else:
            hcn["host"] = [getdet[i].college_name]
    print(hcn)
    return JsonResponse(hcn)
