from django.db import models
# Create your models here.

class clgData(models.Model):
    cname = models.CharField(max_length=50,blank=False,default='')

    def __str__(self):
        return self.cname

class locData(models.Model):
    locstate = models.CharField(max_length=50,blank=False,default='')
    locdistrict = models.CharField(max_length=50,blank=False,default='')
    locemail = models.CharField(max_length=50,blank=False,default='')

    def __str__(self):
        return self.locstate
