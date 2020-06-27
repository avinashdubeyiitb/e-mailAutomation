from django.conf.urls import url,include
from main import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    url(r'^api/main/submit', views.submit),
    url(r'^api/main/approve', views.approve),
    url(r'^api/main/gsave', views.gsave),
    url(r'^api/main/idrequest',views.idrequest),
    url(r'^api/main/csv/submit', views.csvsubmit),
    url(r'^api/main/csv/approve', views.csvapprove),
    url(r'^api/main/csv/gsave', views.csvdraft),
    url(r'^api/main/cwssubmit', views.cwssubmit),
    url(r'^api/main/awssubmit', views.awssubmit),
    url(r'^api/main/getwrklist', views.getwrklist),
    url(r'^api/main/savewrkactv', views.savewrkactv),
    url(r'^api/main/sendmail',views.sendmail),
    url(r'^api/main/getfile',views.getfile),
    url(r'^api/main/formdata',views.formdata),
    url(r'^api/main/headresults',views.headresults),
    url(r'^api/main/form/(?P<uid>[^/]+)/(?P<wid>\w+)/$',views.form),
    url(r'^api/main/headapproval/(?P<uid>[^/]+)/(?P<wid>\w+)/$',views.headapproval),
    url(r'^api/main/store',views.store),
    url(r'^api/main/mailids',views.mailids),
    url(r'^api/main/gethcn',views.gethcn),
    url(r'^api/main/headmail',views.headmail),
    url(r'^api/main/awsedit',views.awsedit),
    url(r'^api/main/awssave',views.awssave),
    url(r'^api/main/login',views.authlogin),
    url(r'^api/main/glogin',views.gauthlogin),
    url(r'^api/main/logout',views.authlogout),
    url(r'^api/main/stats',views.stats),
    # url(r'^api/public/', views.public),
    # url(r'^api/private/', views.private),
    # url(r'^api/main/google', views.GoogleLogin),
    # url(r'^auth/google/',views.GoogleLogin.as_view(), name ='google_login' ),
    url(r'^api/main/algo',views.algo_for_willing_mem)
]