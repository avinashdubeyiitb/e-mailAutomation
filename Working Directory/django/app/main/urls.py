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
]
