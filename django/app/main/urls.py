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
<<<<<<< HEAD
    url(r'^api/main/sendmail',views.sendmail),
    url(r'^api/main/getfile',views.getfile),
    url(r'^api/main/formdata',views.formdata),
    url(r'^api/main/form/(?P<uid>[^/]+)/$',views.form) 
]
=======
    url(r'^api/main/clgdtl',views.collegedetail),
    url(r'^api/main/getfile',views.getfile),
]
>>>>>>> 8b6f71bb6d6a5578eb3191606907e5a696298777
