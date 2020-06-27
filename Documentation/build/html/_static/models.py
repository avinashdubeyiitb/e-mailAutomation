from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    photo = models.URLField(blank=True)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'
        managed = False

class memberdetail(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    emailid = models.EmailField(blank=False,null=False)
    name = models.CharField(max_length=50,blank=False,null=True)
    language = models.TextField(blank=True,null=True)
    team = models.CharField(max_length=10,blank=False,null=True)
    head = models.CharField(max_length=30,blank=False,null=True)
    cohead = models.CharField(max_length=30,blank=False,null=True)
    ishead = models.CharField(max_length=10,blank=False,null=True)
    iscohead = models.CharField(max_length=10,blank=False,null=True)
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'member_detail'

class algo_detail(models.Model):
    demo_module_cnt = models.IntegerField(blank=False,null=False)
    will_ttl_wrkshp_cnt = models.IntegerField(blank=False,null=False)
    aval_ttl_wrkshp_cnt = models.IntegerField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'algo_detail'

class ssn_detail(models.Model):
    ssn_id = models.CharField(max_length=50,blank=False,null=False)
    user = models.CharField(max_length=50,blank=False,null=False)
    timestamp = models.DateTimeField()
    mail_label = models.CharField(max_length=50,blank=False,null=False)
    rcptmailid = models.CharField(max_length=50,blank=False,null=False)
    delegated_access = models.CharField(max_length=10,blank=False,null=False)
    dcprovider = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.user

    class Meta:
        managed = False
        db_table = 'ssn_detail'    

class DemoDtls(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    intro_demo = models.IntegerField(blank=False,null=False)
    i_o_demo = models.IntegerField(blank=False,null=False)
    motor_demo = models.IntegerField(blank=False,null=False)
    pwm_demo = models.IntegerField(blank=False,null=False)
    lcd_demo = models.IntegerField(blank=False,null=False)
    adc_demo = models.IntegerField(blank=False,null=False)
    interrupt_demo = models.IntegerField(blank=False,null=False)
    total_count_demo = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'demo_dtls'
        managed = False

class WorkshopTeamStatus(models.Model):
    workshop_id = models.IntegerField(blank=False,null=False)
    workshop_venue = models.CharField(max_length=100,blank=False,null=False)
    date = models.TextField(blank=False,null=False)
    district = models.CharField(max_length=50,blank=False,null=False)
    responder = models.CharField(max_length=50,blank=False,null=False)
    willingness_or_unavailability = models.CharField(max_length=50,blank=True,null=True,default='None')
    reason = models.CharField(max_length=100,blank=True,null=True)
    eYRC = models.CharField(max_length=50,blank=False,null=True,default='0')
    eYIC = models.CharField(max_length=50,blank=False,null=True,default='0')
    eYRDC = models.CharField(max_length=50,blank=False,null=True,default='0')
    eLSI = models.CharField(max_length=50,blank=False,null=True,default='0')
    web = models.CharField(max_length=50,blank=False,null=True,default='0')
    course_or_other_eyantra_work = models.CharField(max_length=50,blank=False,null=True,default='0')
    personal_or_any_other = models.CharField(max_length=50,blank=False,null=True,default='0')
    approval_eYRC = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_eYIC = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_eYRDC = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_eLSI = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_web = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_course_or_other_eyantra_work = models.CharField(max_length=20,blank=False,null=True,default='None')
    approval_personal_or_any_other = models.CharField(max_length=20,blank=False,null=True,default='None')

    def __str__(self):
        return self.workshop_venue
    class Meta:
        db_table = 'workshop_team_status'
        managed = False

class create_workshop(models.Model):
    id = models.AutoField(primary_key=True)
    hcn = models.TextField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    venueadd = models.TextField(blank=True, null=True)
    cooname = models.TextField(blank=True, null=True)
    cooemail = models.EmailField(blank=False,null=False)
    coono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        managed = False
        db_table = 'create_workshop'
        managed = False

class WorkshopsTakenCount(models.Model):
    name = models.TextField(max_length=50,blank=False,null=False)
    active_member = models.IntegerField(blank=False,null=False)
    preparation_status = models.IntegerField(blank=False,null=False)
    willingness_shown = models.IntegerField(blank=False,null=False)
    total_count = models.IntegerField(blank=False,null=False)
    mumbai_workshop = models.IntegerField(blank=False,null=False)
    non_mumbai_workshop = models.IntegerField(blank=False,null=False)
    total_till_date = models.IntegerField(blank=False,null=False)
    past_year = models.IntegerField(blank=False,null=False)
    past_year_mumbai = models.IntegerField(blank=False,null=False)
    past_year_non_mumbai = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'workshops_taken_count'
        managed = False

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
        managed = False
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
