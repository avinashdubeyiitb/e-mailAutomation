from django.db import models
# Create your models here.

class clgData(models.Model):
    cname = models.CharField(max_length=50,blank=False,default='')

    def __str__(self):
        return self.cname

class editMail(models.Model):
    to = models.EmailField(max_length=50,blank=False,default='')
    ccbcc = models.EmailField(max_length=50,blank=False,default='')
    subject = models.CharField(max_length=50,blank=False,default='')
    body = models.CharField(max_length=500,blank=False,default='')
    attachments = models.CharField(max_length=50,blank=False,default='')  

    def __str__(self):
        return self.to

