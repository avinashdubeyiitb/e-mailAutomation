from django.conf.urls import url
from main import views
from django.contrib import admin
urlpatterns = [
    #url(r'^api/main/csvsubmit', views.csvsubmit),
    url(r'^api/main/submit', views.submit),
    url(r'^api/main/approve', views.approve),
    #url(r'^api/main/edit', views.edit),
    #url(r'^api/main/gsave', views.gsave),
]