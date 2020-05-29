from django.db import models
# Create your models here.

class ElsiCollegeDtls(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    clg_code = models.TextField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    college_type = models.TextField(blank=True, null=True)
    principal_meet = models.IntegerField(blank=True, null=True)
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.TextField(blank=True, null=True)
    eyrtc_allowed = models.IntegerField(blank=True, null=True)
    tbt_allowed = models.IntegerField(blank=True, null=True)
    content_allowed = models.TextField(blank=True, null=True)
    legal_docs = models.TextField(blank=True, null=True)
    legal_docs_remarks = models.TextField(blank=True, null=True)
    loi_status = models.IntegerField(blank=True, null=True)
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.TextField(blank=True, null=True)
    po_status = models.TextField(blank=True, null=True)
    po_remark = models.TextField(blank=True, null=True)
    wo_reg = models.TextField(blank=True, null=True)
    wo_invite = models.TextField(blank=True, null=True)
    wo_confirm = models.TextField(blank=True, null=True)
    wo_attend = models.IntegerField(blank=True, null=True)
    hardware_given = models.TextField(blank=True, null=True)
    lab_inaugurated = models.IntegerField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    eys2016_invites = models.TextField(blank=True, null=True)
    team_verify = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.college_name

    class Meta:
        db_table = 'elsi_college_dtls'

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
