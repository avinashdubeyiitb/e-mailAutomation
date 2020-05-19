from django.db import models
# Create your models here.

class clgData(models.Model):
    cname = models.CharField(max_length=50,blank=False,default='')

    def __str__(self):
        return self.cname

class tempCollegeData(models.Model):
    remail = models.EmailField(max_length=50,blank=False,default='')
    ccbcc = models.EmailField(max_length=50,blank=False,default='')
    name=models.CharField(max_length=50,blank=False,default='')
    designation=models.CharField(max_length=50,blank=False,default='')
    department=models.CharField(max_length=50,blank=False,default='')
    cname=models.CharField(max_length=50,blank=False,default='')
    cno=models.IntegerField()

    def __str__(self):
        return self.name
