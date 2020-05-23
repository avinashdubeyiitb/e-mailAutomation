from django.conf.urls import url
from main import views
from django.contrib import admin
urlpatterns = [
    url(r'^api/main/submit', views.submit),
    url(r'^api/main/approve', views.approve),
    url(r'^api/main/gsave', views.gsave),
    url(r'^api/main/idrequest',views.idrequest),
    url(r'^api/main/csvsubmit', views.csvsubmit),
    url(r'^api/main/save',views.save),
    url(r'^api/main/csvapprove', views.csvapprove),
    url(r'^api/main/csvdraft', views.csvdraft),
]
