from django.db import models
import uuid
# Create your models here.

class userdetail(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    emailid = models.EmailField(blank=False,null=False)
    name = models.CharField(max_length=50,blank=False,null=True)
    def __str__(self):
        return self.emailid
    class Meta:
        db_table = 'userdetail'

class WorkshopTeamDtls(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    workshop_id = models.TextField(blank=False,null=False)
    options = models.CharField(max_length=50,blank=False,null=False)
    category_eyic = models.CharField(max_length=50,blank=False,null=False,default='None')
    category_eyrc = models.CharField(max_length=50,blank=False,null=False,default='None')
    category_eyrdc = models.CharField(max_length=50,blank=False,null=False,default='None')
    category_elsi = models.CharField(max_length=50,blank=False,null=False,default='None')
    category_web = models.CharField(max_length=50,blank=False,null=False,default='None')
    category_others = models.CharField(max_length=50,blank=False,null=False,default='None')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'workshop_team_dtls'

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

class WorkshopParticipants(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_participants'

    def __str__(self):
        return str(self.id)

class WorkshopDtls(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    region_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    active = models.TextField(blank=True, null=True)
    workshop_team = models.TextField(blank=True, null=True)
    start_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_dtls'

    def __str__(self):
        return str(self.id)

class TbtCollegeDtls(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    elsi_clg_id = models.IntegerField(blank=True, null=True)
    region_id = models.TextField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    pincode = models.TextField(blank=True, null=True)
    college_type = models.TextField(blank=True, null=True)
    principal_meet = models.IntegerField(blank=True, null=True)
    robots_given = models.IntegerField(blank=True, null=True)
    tbt_allowed = models.IntegerField(blank=True, null=True)
    tbt_count = models.IntegerField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.TextField(blank=True, null=True)
    loi_status = models.IntegerField(blank=True, null=True)
    po_status = models.TextField(blank=True, null=True)
    po_remark = models.TextField(blank=True, null=True)
    wo_reg = models.TextField(blank=True, null=True)
    wo_invite = models.TextField(blank=True, null=True)
    wo_confirm = models.TextField(blank=True, null=True)
    wo_attend = models.IntegerField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    lab_inaugrated = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_college_dtls'

    def __str__(self):
        return str(self.id)

class AICTE_list(models.Model):
    institute_name = models.TextField()
    state = models.TextField()
    district = models.TextField()
    city = models.TextField()
    full_address = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    class Meta:
        managed = False
        db_table = 'aicte_list'
    def __str__(self):
        return self.institute_name

class ElsiTeacherDtls(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    emailid = models.TextField(blank=True, null=True)
    alt_email1 = models.TextField(blank=True, null=True)
    alt_email2 = models.TextField(blank=True, null=True)
    contact_num = models.TextField(blank=True, null=True)
    alt_contact1 = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    coor_flag = models.IntegerField(blank=True, null=True)
    wo_flag = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    wo_attendee = models.IntegerField(blank=True, null=True)
    wo_count = models.IntegerField(blank=True, null=True)
    eyrtc_flag = models.IntegerField(blank=True, null=True)
    tbt_flag = models.IntegerField(blank=True, null=True)
    eyic_flag = models.TextField(blank=True, null=True)
    content_flag = models.TextField(blank=True, null=True)
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    status_flag = models.TextField(blank=True, null=True)
    modified_by = models.TextField(blank=True, null=True)
    elsi_flag = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    login_created = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_teacher_dtls'
