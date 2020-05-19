from django.conf.urls import url
from main import views
from django.contrib import admin
urlpatterns = [
    url(r'^api/main/savefile', views.savefile),
    url(r'^api/main/submit', views.submit),
    url(r'^api/main/approve', views.approve),
    url(r'^api/main/gsave', views.gsave),
]
