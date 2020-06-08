from django.conf.urls import url
from main import views
from django.contrib import admin
urlpatterns = [
    url(r'^api/main/submit', views.submit),
    url(r'^api/main/approve', views.approve),
    url(r'^api/main/gsave', views.gsave),
    url(r'^api/main/idrequest',views.idrequest),
    url(r'^api/main/csv/submit', views.csvsubmit),
    url(r'^api/main/save',views.save),
    url(r'^api/main/csv/approve', views.csvapprove),
    url(r'^api/main/csv/gsave', views.csvdraft),
    url(r'^api/main/awssubmit', views.awssubmit),
    url(r'^api/main/sendmail',views.sendmail),
    url(r'^api/main/getfile',views.getfile),
    url(r'^api/main/formdata',views.formdata),
    url(r'^api/main/form/(?P<uid>[^/]+)/$',views.form),
    url(r'^api/main/store',views.store),
    url(r'^api/main/mailids',views.mailids)
]
