# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdvancedWorkshop(models.Model):
    clg_code = models.CharField(max_length=250)
    name = models.CharField(max_length=512)
    emailid = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    contact_num = models.CharField(max_length=11)
    alt_contact1 = models.CharField(max_length=11, blank=True, null=True)
    designation = models.CharField(max_length=250)
    role = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advanced_workshop'


class AlumniEmail(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    email_flag = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alumni_email'


class BackupElsiCollegeDtls(models.Model):
    clg_code = models.CharField(max_length=512, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField()
    college_name = models.CharField(max_length=1024)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    college_type = models.CharField(max_length=256, blank=True, null=True)
    principal_meet = models.IntegerField()
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.IntegerField()
    eyrtc_allowed = models.IntegerField()
    tbt_allowed = models.IntegerField()
    content_allowed = models.IntegerField()
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.CharField(max_length=1024, blank=True, null=True)
    loi_status = models.IntegerField()
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.CharField(max_length=1024, blank=True, null=True)
    po_status = models.IntegerField(blank=True, null=True)
    po_remark = models.CharField(max_length=1024, blank=True, null=True)
    wo_reg = models.IntegerField()
    wo_invite = models.IntegerField()
    wo_confirm = models.IntegerField()
    wo_attend = models.IntegerField()
    hardware_given = models.CharField(max_length=1024, blank=True, null=True)
    lab_inaugurated = models.IntegerField()
    phase = models.IntegerField()
    eys2016_invites = models.IntegerField()
    team_verify = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backup_elsi_college_dtls'


class CollegesToContactToEstablishElsi(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    college_name = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    designation = models.CharField(max_length=512, blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colleges_to_contact_to_establish_elsi'


class ConFeedback(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    curriculum = models.CharField(max_length=20, blank=True, null=True)
    lab_exp = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    lesson_id = models.IntegerField(blank=True, null=True)
    lesson_plan_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_feedback'


class ConLatex(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    down_date = models.CharField(max_length=200, blank=True, null=True)
    flag = models.IntegerField()
    upload_date = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    accept_reject = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_latex'


class ConLessonCreate(models.Model):
    lp_name = models.TextField(blank=True, null=True)
    lp_plan = models.CharField(max_length=100, blank=True, null=True)
    refer_content = models.TextField()
    available = models.IntegerField()
    tch_count = models.IntegerField(blank=True, null=True)
    i_agree = models.IntegerField()
    phase = models.IntegerField()
    launch_date = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_lesson_create'


class ConLessonPlanList(models.Model):
    name = models.CharField(max_length=1024)
    image_name = models.CharField(max_length=1024, blank=True, null=True)
    short_intro = models.CharField(max_length=2048, blank=True, null=True)
    intro_video_code = models.CharField(max_length=512, blank=True, null=True)
    available = models.IntegerField()
    student_chk = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_lesson_plan_list'


class ConLessonPlanLongContent(models.Model):
    lesson_plan_id = models.IntegerField()
    long_intro = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_lesson_plan_long_content'


class ConLpLessons(models.Model):
    lesson_plan_id = models.IntegerField()
    display_num = models.IntegerField()
    lesson_name = models.CharField(max_length=512)
    video1_code = models.CharField(max_length=512, blank=True, null=True)
    video1_name = models.CharField(max_length=1024, blank=True, null=True)
    video2_code = models.CharField(max_length=512, blank=True, null=True)
    video2_name = models.CharField(max_length=1024, blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    down_tm = models.IntegerField()
    count_tm = models.IntegerField()
    down_rr = models.IntegerField()
    count_rr = models.IntegerField()
    down_qb = models.IntegerField()
    count_qb = models.IntegerField()
    down_qbs = models.IntegerField()
    count_qbs = models.IntegerField()
    down_le = models.IntegerField()
    count_le = models.IntegerField()
    down_les = models.IntegerField()
    count_les = models.IntegerField(blank=True, null=True)
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_lp_lessons'


class ConProjectGeneric(models.Model):
    name = models.CharField(max_length=1024)
    video_url = models.CharField(max_length=1024, blank=True, null=True)
    type = models.IntegerField()
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_project_generic'


class ConProjectList(models.Model):
    name = models.CharField(max_length=1024)
    image_name = models.CharField(max_length=1024, blank=True, null=True)
    report_name = models.CharField(max_length=50)
    available = models.IntegerField()
    count_project = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_project_list'


class ConProjectTopics(models.Model):
    proj_id = models.IntegerField()
    hardware = models.TextField()
    software = models.TextField(blank=True, null=True)
    authors = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_code = models.CharField(max_length=512, blank=True, null=True)
    code_link = models.CharField(max_length=512, blank=True, null=True)
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_project_topics'


class ConRegistration(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    name_cheq = models.CharField(max_length=200, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    branch = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_registration'


class ConSuggestedTopic(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    choice = models.CharField(max_length=200, blank=True, null=True)
    email_sent = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_suggested_topic'


class ConTemplate(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    lesson_id = models.IntegerField(blank=True, null=True)
    i_agree = models.IntegerField()
    start_date = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.CharField(max_length=200, blank=True, null=True)
    flag = models.IntegerField()
    upload_date = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)
    lp8051 = models.TextField(blank=True, null=True)
    lparm = models.TextField(blank=True, null=True)
    down_rev_les = models.IntegerField()
    upload_rev_date = models.CharField(max_length=256, blank=True, null=True)
    rev_upld_date = models.CharField(max_length=200, blank=True, null=True)
    rev_status = models.TextField(blank=True, null=True)
    rev_flag = models.IntegerField(blank=True, null=True)
    accept_reject = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    plag = models.CharField(max_length=100, blank=True, null=True)
    reg_status = models.IntegerField()
    agreement = models.IntegerField(blank=True, null=True)
    reviewer_name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'con_template'


class ConTutorialCreate(models.Model):
    tut_name = models.CharField(max_length=100, blank=True, null=True)
    tut_plan = models.CharField(max_length=100, blank=True, null=True)
    refer_content = models.TextField()
    available = models.IntegerField()
    tch_count = models.IntegerField(blank=True, null=True)
    i_agree = models.IntegerField()
    phase = models.IntegerField()
    launch_date = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_tutorial_create'


class ConTutorialList(models.Model):
    name = models.CharField(max_length=1024)
    image_name = models.CharField(max_length=1024, blank=True, null=True)
    short_intro = models.CharField(max_length=2048, blank=True, null=True)
    intro_video_code = models.CharField(max_length=512, blank=True, null=True)
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_tutorial_list'


class ConTutorialLongContent(models.Model):
    tut_id = models.IntegerField()
    long_intro = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_tutorial_long_content'


class ConTutorialTopics(models.Model):
    tut_id = models.IntegerField()
    display_num = models.IntegerField()
    topic_name = models.CharField(max_length=512)
    video_code = models.CharField(max_length=512, blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    down_code = models.IntegerField()
    down_ppt = models.IntegerField()
    down_misc = models.IntegerField()
    count_ppt = models.IntegerField()
    count_code = models.IntegerField()
    count_misc = models.IntegerField()
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_tutorial_topics'


class ConVideoStage0(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    video_link = models.TextField(blank=True, null=True)
    submit_date = models.TextField()
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_video_stage0'


class ContentCount(models.Model):
    clg_id = models.IntegerField()
    username = models.CharField(unique=True, max_length=512)
    content = models.IntegerField()
    down_tm = models.IntegerField()
    down_rr = models.IntegerField()
    down_qb = models.IntegerField()
    down_qbs = models.IntegerField()
    down_le = models.IntegerField()
    down_les = models.IntegerField()
    ie_mod = models.IntegerField()
    down_tut_ppt = models.IntegerField()
    down_tut_code = models.IntegerField()
    down_tut_misc = models.IntegerField()
    count_lecture = models.IntegerField()
    down_project = models.IntegerField()
    down_lesson_temp = models.IntegerField()
    down_latex = models.IntegerField()
    down_video_res = models.IntegerField()
    down_stg1_temp = models.IntegerField()
    down_res_tutorial = models.IntegerField()
    create_content = models.IntegerField()
    blockly = models.IntegerField(blank=True, null=True)
    suggest = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_count'


class ContentRegister(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    designation = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    upload = models.CharField(max_length=40, blank=True, null=True)
    accept_reject = models.TextField(blank=True, null=True)
    email_flag = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'content_register'


class CreateTutorial(models.Model):
    tch_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tut_id = models.IntegerField(blank=True, null=True)
    i_agree = models.IntegerField()
    start_date = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.CharField(max_length=200, blank=True, null=True)
    video_link = models.TextField(blank=True, null=True)
    rev_video_link = models.TextField(blank=True, null=True)
    tut_explain = models.TextField(blank=True, null=True)
    flag = models.IntegerField()
    upload_date = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)
    lp8051 = models.TextField(blank=True, null=True)
    lparm = models.TextField(blank=True, null=True)
    down_rev_tuto = models.IntegerField()
    upload_rev_date = models.CharField(max_length=256, blank=True, null=True)
    rev_upld_date = models.CharField(max_length=200, blank=True, null=True)
    rev_status = models.TextField(blank=True, null=True)
    rev_flag = models.IntegerField()
    accept_reject = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    plag = models.CharField(max_length=100, blank=True, null=True)
    reg_status = models.IntegerField()
    agreement = models.IntegerField()
    reviewer_name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'create_tutorial'


class ElsiClgContactDtl(models.Model):
    clg_id = models.IntegerField()
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=12, blank=True, null=True)
    branch = models.CharField(max_length=128, blank=True, null=True)
    alt_email1 = models.CharField(max_length=256, blank=True, null=True)
    alt_email2 = models.CharField(max_length=256, blank=True, null=True)
    alt_email3 = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=50, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=50, blank=True, null=True)
    alt_contact2 = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField()
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    status_cnt = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_clg_contact_dtl'


class ElsiCollegeDtls(models.Model):
    clg_code = models.CharField(max_length=512, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField()
    college_name = models.CharField(max_length=1024)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    college_type = models.CharField(max_length=256, blank=True, null=True)
    principal_meet = models.IntegerField()
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.IntegerField()
    eyrtc_allowed = models.IntegerField()
    tbt_allowed = models.IntegerField()
    mooc_allowed = models.IntegerField(blank=True, null=True)
    content_allowed = models.IntegerField()
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.CharField(max_length=1024, blank=True, null=True)
    loi_status = models.IntegerField()
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.CharField(max_length=1024, blank=True, null=True)
    po_status = models.IntegerField(blank=True, null=True)
    po_remark = models.CharField(max_length=1024, blank=True, null=True)
    wo_reg = models.IntegerField()
    wo_invite = models.IntegerField()
    wo_confirm = models.IntegerField()
    wo_attend = models.IntegerField()
    hardware_given = models.CharField(max_length=1024, blank=True, null=True)
    lab_inaugurated = models.IntegerField()
    phase = models.IntegerField()
    eys2016_invites = models.IntegerField()
    team_verify = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_college_dtls'


class ElsiCompetitions(models.Model):
    year = models.CharField(max_length=12)
    name = models.CharField(max_length=256, blank=True, null=True)
    theme = models.CharField(max_length=256, blank=True, null=True)
    phase = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_competitions'


class ElsiDepartments(models.Model):
    name = models.CharField(max_length=512)
    main_branch = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_departments'


class ElsiDesignations(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_designations'


class ElsiEmails(models.Model):
    subject = models.CharField(max_length=2054)
    email_msg = models.CharField(max_length=5200, blank=True, null=True)
    img = models.CharField(max_length=1024, blank=True, null=True)
    pdf = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_emails'


class ElsiMooc(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    clg_code = models.CharField(max_length=200, blank=True, null=True)
    college_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    slot = models.CharField(max_length=200, blank=True, null=True)
    email_flag = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_mooc'

'''
class ElsiRegion(models.Model):
    region_name = models.CharField(max_length=512)
    type = models.IntegerField()
    active = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_region'
'''

class ElsiState(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_state'


class ElsiStudentsMooc(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    clg = models.ForeignKey(ElsiCollegeDtls, models.DO_NOTHING, blank=True, null=True)
    emailid = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=12, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=12, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    current_year = models.CharField(max_length=5, blank=True, null=True)
    mooc_allowed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_students_mooc'


class ElsiTeachersDtls(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    alt_email1 = models.CharField(max_length=256, blank=True, null=True)
    alt_email2 = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    designation = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    coor_flag = models.IntegerField()
    wo_flag = models.IntegerField()
    mooc_allowed = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField()
    wo_attendee = models.IntegerField()
    wo_count = models.IntegerField()
    eyrtc_flag = models.IntegerField()
    tbt_flag = models.IntegerField()
    eyic_flag = models.IntegerField()
    content_flag = models.IntegerField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=150, blank=True, null=True)  # Field name made lowercase.
    status_flag = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    elsi_flag = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    login_created = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_teachers_dtls'


class EyantraCertDtls(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    tch_id = models.IntegerField(blank=True, null=True)
    cert_num = models.CharField(max_length=200, blank=True, null=True)
    cert_date = models.CharField(max_length=25, blank=True, null=True)
    generated_at = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    eyrtc_id = models.IntegerField(blank=True, null=True)
    eyic_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eyantra_cert_dtls'


class EyrtcParticipation(models.Model):
    clg_id = models.IntegerField()
    comp_id = models.IntegerField()
    tl_id = models.IntegerField()
    tm1_id = models.IntegerField(blank=True, null=True)
    tm2_id = models.IntegerField(blank=True, null=True)
    tm3_id = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eyrtc_participation'


class EyrtcStatus(models.Model):
    part_id = models.IntegerField()
    task0_uploaded = models.IntegerField()
    task0_date = models.DateTimeField(blank=True, null=True)
    task0_file_name = models.CharField(max_length=200, blank=True, null=True)
    task0_marks = models.FloatField(blank=True, null=True)
    task0_remark = models.CharField(max_length=1024, blank=True, null=True)
    task1_uploaded = models.IntegerField()
    task1_date = models.DateTimeField(blank=True, null=True)
    task1_link = models.CharField(max_length=1024, blank=True, null=True)
    task1_marks = models.FloatField(blank=True, null=True)
    task1_remark = models.CharField(max_length=1024, blank=True, null=True)
    task2_uploaded = models.IntegerField()
    task2_date = models.DateTimeField(blank=True, null=True)
    task2_link1 = models.CharField(max_length=2048, blank=True, null=True)
    task2_link2 = models.CharField(max_length=2048, blank=True, null=True)
    task2_marks = models.FloatField(blank=True, null=True)
    task2_remark = models.CharField(max_length=1024, blank=True, null=True)
    taskvideo_uploaded = models.IntegerField()
    taskvideo_date = models.DateTimeField(blank=True, null=True)
    taskvideo_link = models.CharField(max_length=2048, blank=True, null=True)
    taskvideo_marks = models.FloatField(blank=True, null=True)
    taskvideo_remark = models.CharField(max_length=1024, blank=True, null=True)
    taskcode_uploaded = models.IntegerField()
    taskcode_date = models.DateTimeField(blank=True, null=True)
    taskcode_marks = models.FloatField(blank=True, null=True)
    taskcode_remark = models.CharField(max_length=1024, blank=True, null=True)
    final_validatory_marks = models.IntegerField(blank=True, null=True)
    final_validatory_remarks = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eyrtc_status'


class EysRegistration2016(models.Model):
    part_id = models.IntegerField()
    clg_id = models.IntegerField()
    team_id = models.CharField(max_length=2056, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    arrival_date = models.CharField(max_length=256, blank=True, null=True)
    departure_date = models.CharField(max_length=256, blank=True, null=True)
    elsi_coor = models.IntegerField()
    elsi_competition = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=512, blank=True, null=True)
    accommodation = models.CharField(max_length=512, blank=True, null=True)
    attendence = models.CharField(max_length=512, blank=True, null=True)
    reached_venue = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eys_registration_2016'


class EysRegistration2017(models.Model):
    part_id = models.IntegerField()
    clg_id = models.IntegerField()
    team_id = models.CharField(max_length=2056, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    arrival_date = models.CharField(max_length=256, blank=True, null=True)
    arrival_time = models.CharField(max_length=250, blank=True, null=True)
    departure_date = models.CharField(max_length=256, blank=True, null=True)
    elsi_coor = models.IntegerField()
    elsi_competition = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=512, blank=True, null=True)
    accommodation = models.CharField(max_length=512, blank=True, null=True)
    attendence = models.CharField(max_length=512, blank=True, null=True)
    account_number = models.CharField(max_length=512, blank=True, null=True)
    account_holder_name = models.CharField(max_length=512, blank=True, null=True)
    bank_name = models.CharField(max_length=512, blank=True, null=True)
    bank_address = models.CharField(max_length=512, blank=True, null=True)
    account_type = models.CharField(max_length=512, blank=True, null=True)
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=512, blank=True, null=True)  # Field name made lowercase.
    reached_venue = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eys_registration_2017'


class EysRegistration2018(models.Model):
    part_id = models.IntegerField()
    clg_id = models.IntegerField()
    team_id = models.CharField(max_length=2056, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    arrival_date = models.CharField(max_length=256, blank=True, null=True)
    arrival_time = models.CharField(max_length=250, blank=True, null=True)
    departure_date = models.CharField(max_length=256, blank=True, null=True)
    elsi_coor = models.IntegerField()
    elsi_competition = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=512, blank=True, null=True)
    accommodation = models.CharField(max_length=512, blank=True, null=True)
    attendence = models.CharField(max_length=512, blank=True, null=True)
    account_number = models.CharField(max_length=512, blank=True, null=True)
    account_holder_name = models.CharField(max_length=512, blank=True, null=True)
    bank_name = models.CharField(max_length=512, blank=True, null=True)
    bank_address = models.CharField(max_length=512, blank=True, null=True)
    account_type = models.CharField(max_length=512, blank=True, null=True)
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=512, blank=True, null=True)  # Field name made lowercase.
    reached_venue = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eys_registration_2018'


class EysRegistration2019(models.Model):
    part_id = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    team_id = models.CharField(max_length=2056, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    arrival_date = models.CharField(max_length=256, blank=True, null=True)
    arrival_time = models.CharField(max_length=250, blank=True, null=True)
    departure_date = models.CharField(max_length=256, blank=True, null=True)
    elsi_coor = models.IntegerField()
    elsi_competition = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=512, blank=True, null=True)
    accommodation = models.CharField(max_length=512, blank=True, null=True)
    attendence = models.CharField(max_length=512, blank=True, null=True)
    account_number = models.CharField(max_length=512, blank=True, null=True)
    account_holder_name = models.CharField(max_length=512, blank=True, null=True)
    bank_name = models.CharField(max_length=512, blank=True, null=True)
    bank_address = models.CharField(max_length=512, blank=True, null=True)
    account_type = models.CharField(max_length=512, blank=True, null=True)
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=512, blank=True, null=True)  # Field name made lowercase.
    reached_venue = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eys_registration_2019'


class EysRegistration2020(models.Model):
    part_id = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    team_id = models.CharField(max_length=2056, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    arrival_date = models.CharField(max_length=256, blank=True, null=True)
    arrival_time = models.CharField(max_length=250, blank=True, null=True)
    departure_date = models.CharField(max_length=256, blank=True, null=True)
    elsi_coor = models.IntegerField()
    elsi_competition = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=512, blank=True, null=True)
    accommodation = models.CharField(max_length=512, blank=True, null=True)
    attendence = models.CharField(max_length=512, blank=True, null=True)
    account_number = models.CharField(max_length=512, blank=True, null=True)
    account_holder_name = models.CharField(max_length=512, blank=True, null=True)
    bank_name = models.CharField(max_length=512, blank=True, null=True)
    bank_address = models.CharField(max_length=512, blank=True, null=True)
    account_type = models.CharField(max_length=512, blank=True, null=True)
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=512, blank=True, null=True)  # Field name made lowercase.
    reached_venue = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eys_registration_2020'


class EysipConduct(models.Model):
    stud_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    photograph = models.CharField(max_length=100, blank=True, null=True)
    pancard = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    conduct = models.IntegerField(blank=True, null=True)
    proj_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eysip_conduct'


class IeModules(models.Model):
    name = models.CharField(max_length=1024)
    image_name = models.CharField(max_length=1024, blank=True, null=True)
    short_intro = models.CharField(max_length=2048, blank=True, null=True)
    video_code = models.CharField(max_length=512, blank=True, null=True)
    down_pdf = models.CharField(max_length=1024, blank=True, null=True)
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ie_modules'


class Login(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    team_id = models.IntegerField()
    team_member_id = models.IntegerField()
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=1024)
    role = models.IntegerField()
    active = models.IntegerField()
    theme = models.CharField(max_length=20, blank=True, null=True)
    email_flag = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    change_count = models.IntegerField()
    forgot_count = models.IntegerField()
    remember_token = models.CharField(max_length=1024, blank=True, null=True)
    verify_token = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=1024, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class LoginEmails(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_member_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=1024, blank=True, null=True)
    role = models.IntegerField()
    active = models.IntegerField()
    theme = models.CharField(max_length=20, blank=True, null=True)
    email_flag = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    login_count = models.IntegerField()
    change_count = models.IntegerField()
    forgot_count = models.IntegerField()
    remember_token = models.CharField(max_length=1024, blank=True, null=True)
    verify_token = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=1024, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_emails'


class MoocColleges(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    tch_email = models.CharField(max_length=200, blank=True, null=True)
    students = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mooc_colleges'


class OnlineLabInauguration(models.Model):
    clg_id = models.IntegerField()
    labinaug_date = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_lab_inauguration'


class PrincipalMeetAttendee(models.Model):
    principal_meet_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=250, blank=True, null=True)
    contact_num = models.CharField(max_length=100, blank=True, null=True)
    alt_contact1 = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    designation = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'principal_meet_attendee'


class PrincipalMeetDtls(models.Model):
    region_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principal_meet_dtls'


class PrincipalMeetParticipants(models.Model):
    principal_meet_id = models.IntegerField(blank=True, null=True)
    data_table_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    clg_contact_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'principal_meet_participants'

'''
class RegionalFinalsInvite(models.Model):
    id = models.AutoField(unique=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    college_name = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=300, blank=True, null=True)
    regional = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    attendees = models.IntegerField(blank=True, null=True)
    lunch = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regional_finals_invite'
'''
'''
class RegionalFinalsInviteToBeSent(models.Model):
    id = models.AutoField(unique=True)
    college_name = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    designation = models.CharField(max_length=512, blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    venue = models.CharField(max_length=512, blank=True, null=True)
    day2 = models.CharField(max_length=512, blank=True, null=True)
    daydate = models.CharField(max_length=512, blank=True, null=True)
    subject = models.CharField(max_length=200)
    attach = models.CharField(max_length=200)
    rsvpname = models.CharField(max_length=100)
    rsvpemail = models.CharField(max_length=100)
    rsvpcontact = models.CharField(max_length=100)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regional_finals_invite_to_be_sent'
'''

class Talks(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    image_alt = models.CharField(max_length=128, blank=True, null=True)
    short_intro = models.TextField(blank=True, null=True)
    visited_lecture = models.IntegerField()
    available = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talks'


class TalksSeries(models.Model):
    display = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=512, blank=True, null=True)
    img_url = models.CharField(max_length=512, blank=True, null=True)
    available = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talks_series'


class TbtChallengeStatus(models.Model):
    part_id = models.IntegerField()
    i_agree_challenge = models.IntegerField()
    task1_uploaded = models.IntegerField()
    task1_upload_time = models.DateTimeField()
    task1_file_name = models.CharField(max_length=64, blank=True, null=True)
    task1_marks = models.FloatField(blank=True, null=True)
    task1_remark = models.CharField(max_length=1024, blank=True, null=True)
    task2_uploaded = models.IntegerField()
    task2_video_link = models.CharField(max_length=256, blank=True, null=True)
    task2_upload_time = models.DateTimeField(blank=True, null=True)
    task2_code_uploaded = models.IntegerField()
    task2_code_upload_time = models.DateTimeField(blank=True, null=True)
    task2_marks = models.FloatField(blank=True, null=True)
    task2_remark = models.CharField(max_length=1024, blank=True, null=True)
    challenge_result = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_challenge_status'

'''
class TbtFeedback(models.Model):
    clg_id = models.IntegerField()
    usr_id = models.IntegerField()
    teacher_name = models.CharField(max_length=1024)
    email_id = models.CharField(max_length=1024, blank=True, null=True)
    question1 = models.TextField(blank=True, null=True)
    question2 = models.TextField(blank=True, null=True)
    question3 = models.TextField(blank=True, null=True)
    question4 = models.TextField(blank=True, null=True)
    question5 = models.TextField(blank=True, null=True)
    question6 = models.TextField(blank=True, null=True)
    question7 = models.CharField(max_length=8192, blank=True, null=True)
    question8 = models.CharField(max_length=8192, blank=True, null=True)
    question9 = models.CharField(max_length=8192, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_feedback'
'''

class TbtParticipation(models.Model):
    clg_id = models.IntegerField()
    tbt_phase = models.IntegerField()
    tl_id = models.IntegerField()
    tm1_id = models.IntegerField(blank=True, null=True)
    tm2_id = models.IntegerField(blank=True, null=True)
    tm3_id = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_participation'


class TbtQuesAnsDtls(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    part_id = models.IntegerField(blank=True, null=True)
    ques_1 = models.IntegerField(blank=True, null=True)
    ques_2 = models.IntegerField(blank=True, null=True)
    ques_3 = models.IntegerField(blank=True, null=True)
    ques_4 = models.IntegerField(blank=True, null=True)
    ques_5 = models.CharField(max_length=1024, blank=True, null=True)
    task = models.IntegerField(blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    total_marks = models.FloatField(blank=True, null=True)
    save_count = models.IntegerField(blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_ques_ans_dtls'


class TbtQuestionMaster(models.Model):
    question = models.IntegerField(blank=True, null=True)
    option_1 = models.IntegerField(blank=True, null=True)
    option_2 = models.IntegerField(blank=True, null=True)
    option_3 = models.IntegerField(blank=True, null=True)
    option_4 = models.IntegerField(blank=True, null=True)
    option_5 = models.IntegerField(blank=True, null=True)
    correct_option = models.IntegerField(blank=True, null=True)
    task = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_question_master'


class TbtStatus(models.Model):
    part_id = models.IntegerField()
    task1_uploaded = models.IntegerField()
    task1_upload_time = models.DateTimeField()
    task1_marks = models.FloatField(blank=True, null=True)
    task1_remark = models.CharField(max_length=1024, blank=True, null=True)
    task2_uploaded = models.IntegerField()
    task2_upload_time = models.DateTimeField(blank=True, null=True)
    task2_marks = models.FloatField(blank=True, null=True)
    task2_remark = models.CharField(max_length=1024, blank=True, null=True)
    task3_uploaded = models.IntegerField()
    task3_upload_time = models.DateTimeField()
    task3_marks = models.FloatField(blank=True, null=True)
    task3_remark = models.CharField(max_length=1024, blank=True, null=True)
    task4_uploaded = models.IntegerField()
    task4_upload_time = models.DateTimeField()
    task4_marks = models.FloatField(blank=True, null=True)
    task4_remark = models.CharField(max_length=1024, blank=True, null=True)
    task5_uploaded = models.IntegerField()
    task5_upload_time = models.DateTimeField()
    task5_marks = models.FloatField(blank=True, null=True)
    task5_remark = models.CharField(max_length=1024, blank=True, null=True)
    task6_uploaded = models.IntegerField()
    task6_upload_time = models.DateTimeField()
    task6_marks = models.FloatField(blank=True, null=True)
    task6_remark = models.CharField(max_length=1024, blank=True, null=True)
    award_grade = models.CharField(max_length=64, blank=True, null=True)
    names_ok = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_status'

'''
class TbtTempData(models.Model):
    id = models.AutoField(unique=True)
    region_id = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=1024, blank=True, null=True)
    abbreviated = models.CharField(max_length=32, blank=True, null=True)
    district = models.CharField(max_length=512, blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    polytech = models.IntegerField(blank=True, null=True)
    principal_name = models.CharField(max_length=256, blank=True, null=True)
    principal_contact = models.CharField(max_length=16, blank=True, null=True)
    principal_email = models.CharField(max_length=256, blank=True, null=True)
    college_address = models.CharField(max_length=2048, blank=True, null=True)
    tm1_name = models.CharField(max_length=256, blank=True, null=True)
    tm1_email = models.CharField(max_length=256, blank=True, null=True)
    tm1_contact = models.BigIntegerField(blank=True, null=True)
    tm1_role = models.IntegerField(blank=True, null=True)
    tm1_wrk = models.IntegerField(blank=True, null=True)
    tm2_name = models.CharField(max_length=256, blank=True, null=True)
    tm2_email = models.CharField(max_length=256, blank=True, null=True)
    tm2_contact = models.BigIntegerField(blank=True, null=True)
    tm2_role = models.IntegerField(blank=True, null=True)
    tm2_wrk = models.IntegerField(blank=True, null=True)
    tm3_name = models.CharField(max_length=256, blank=True, null=True)
    tm3_email = models.CharField(max_length=256, blank=True, null=True)
    tm3_contact = models.BigIntegerField(blank=True, null=True)
    tm3_role = models.IntegerField(blank=True, null=True)
    tm3_wrk = models.IntegerField(blank=True, null=True)
    tm4_name = models.CharField(max_length=256, blank=True, null=True)
    tm4_email = models.CharField(max_length=256, blank=True, null=True)
    tm4_contact = models.BigIntegerField(blank=True, null=True)
    tm4_role = models.IntegerField(blank=True, null=True)
    tm4_wrk = models.IntegerField(blank=True, null=True)
    tm5_name = models.CharField(max_length=256, blank=True, null=True)
    tm5_email = models.CharField(max_length=256, blank=True, null=True)
    tm5_contact = models.BigIntegerField(blank=True, null=True)
    tm5_role = models.IntegerField(blank=True, null=True)
    tm5_wrk = models.IntegerField(blank=True, null=True)
    loi_status = models.IntegerField(blank=True, null=True)
    robots_given = models.IntegerField(blank=True, null=True)
    login_allowed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_temp_data'

'''
class TeamEmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    contact = models.CharField(unique=True, max_length=15)
    discipline_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    role = models.IntegerField()
    eyrc_year = models.CharField(max_length=1024, blank=True, null=True)
    eyrc_theme = models.CharField(max_length=1024, blank=True, null=True)
    eyrc_cert = models.CharField(max_length=1024, blank=True, null=True)
    tracking = models.CharField(max_length=250, blank=True, null=True)
    dispatch_date = models.TextField(blank=True, null=True)
    email_flag = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_email'


class TeamMemberDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    flag = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_member_detail'


class TempCollege(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField()
    college_name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024, blank=True, null=True)
    principal_meet = models.IntegerField()
    work_shop = models.IntegerField()
    current_stat = models.IntegerField(blank=True, null=True)
    principalname = models.CharField(db_column='PrincipalName', max_length=512, blank=True, null=True)  # Field name made lowercase.
    p_number = models.CharField(db_column='P_Number', max_length=256, blank=True, null=True)  # Field name made lowercase.
    p_number2 = models.CharField(db_column='P_Number2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    p_emailid = models.CharField(db_column='P_emailID', max_length=512, blank=True, null=True)  # Field name made lowercase.
    loi_status = models.IntegerField()
    college_updated = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_college'


class TempElsiCollegeDtls(models.Model):
    id = models.IntegerField(primary_key=True)
    clg_code = models.CharField(max_length=512, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField()
    college_name = models.CharField(max_length=1024)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    college_type = models.CharField(max_length=256, blank=True, null=True)
    principal_meet = models.IntegerField()
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.IntegerField()
    eyrtc_allowed = models.IntegerField()
    tbt_allowed = models.IntegerField()
    content_allowed = models.IntegerField()
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.CharField(max_length=1024, blank=True, null=True)
    loi_status = models.IntegerField()
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.CharField(max_length=1024, blank=True, null=True)
    po_status = models.IntegerField(blank=True, null=True)
    po_remark = models.CharField(max_length=1024, blank=True, null=True)
    wo_reg = models.IntegerField()
    wo_invite = models.IntegerField()
    wo_confirm = models.IntegerField()
    wo_attend = models.IntegerField()
    hardware_given = models.CharField(max_length=1024, blank=True, null=True)
    lab_inaugurated = models.IntegerField()
    phase = models.IntegerField()
    eys2016_invites = models.IntegerField()
    team_verify = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_elsi_college_dtls'


class TempPrincipalMeet(models.Model):
    region_id = models.IntegerField()
    temp_clg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    contact_num = models.CharField(max_length=100, blank=True, null=True)
    alt_contact_num1 = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=512, blank=True, null=True)
    clg_type = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_principal_meet'


class TempWorkshopAttend(models.Model):
    temp_clg_id = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField()
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=256)
    contact_num = models.CharField(max_length=256)
    alternate_email1 = models.CharField(max_length=512, blank=True, null=True)
    department = models.CharField(max_length=216, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    workshop_attend = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_workshop_attend'

'''
class UsersLogin(models.Model):
    clg_id = models.IntegerField()
    username = models.CharField(unique=True, max_length=512)
    password = models.CharField(max_length=1024, blank=True, null=True)
    admin = models.IntegerField()
    content = models.IntegerField()
    cont_flag = models.IntegerField()
    eyrtc = models.IntegerField()
    tbt = models.IntegerField()
    active = models.IntegerField()
    agree = models.IntegerField()
    token = models.CharField(max_length=1024, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    change_count = models.IntegerField()
    forgot_count = models.IntegerField()
    incorrect_login_attempts = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_login'
'''

class VerificationTokens(models.Model):
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    expires_in = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verification_tokens'


class WorkshopDtls(models.Model):
    region_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    workshop_team = models.CharField(max_length=520)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_dtls'


class WorkshopParticipants(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_participants'


class WorkshopShipmentDtls(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    shipment_date = models.DateField(blank=True, null=True)
    tracking_no = models.IntegerField(blank=True, null=True)
    mode_of_dispatch = models.CharField(max_length=1024, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'workshop_shipment_dtls'


class WorkshopTeam(models.Model):
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workshop_team'
