from django.db import models
# Create your models here.

class collegeData(models.Model):
    mail_id = models.EmailField()
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    contact=models.IntegerField()
    def __str__(self):
        return self.college
