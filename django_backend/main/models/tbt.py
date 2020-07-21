# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=512)
    main_branch = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Designations(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designations'


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


class Region(models.Model):
    region_name = models.CharField(max_length=512)
    type = models.IntegerField()
    active = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class State(models.Model):
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class TbtChallengeMaster(models.Model):
    theme = models.CharField(max_length=255)
    description = models.CharField(max_length=1020, blank=True, null=True)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_challenge_master'


class TbtChallengeTeamSchedule(models.Model):
    team_id = models.IntegerField()
    theme_id = models.IntegerField()
    launch_date = models.DateTimeField()
    task1_deadline = models.DateTimeField()
    task2_deadline = models.DateTimeField()
    tbt_phase = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_challenge_team_schedule'


class TbtClgContactDtls(models.Model):
    tbt_clg_id = models.IntegerField()
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
    alt_contact3 = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_clg_contact_dtls'


class TbtCollegeDtls(models.Model):
    elsi_clg_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=1024)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    college_type = models.CharField(max_length=256, blank=True, null=True)
    principal_meet = models.IntegerField()
    robots_given = models.IntegerField(blank=True, null=True)
    tbt_allowed = models.IntegerField()
    tbt_count = models.IntegerField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.CharField(max_length=1024, blank=True, null=True)
    loi_status = models.IntegerField(blank=True, null=True)
    po_status = models.IntegerField(blank=True, null=True)
    po_remark = models.CharField(max_length=1024, blank=True, null=True)
    wo_reg = models.IntegerField()
    wo_invite = models.IntegerField()
    wo_confirm = models.IntegerField()
    wo_attend = models.IntegerField()
    phase = models.IntegerField()
    lab_inaugrated = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_college_dtls'


class TbtCompetition(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=16)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_competition'


class TbtExperimentMaster(models.Model):
    task_id = models.IntegerField()
    ex_version_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_experiment_master'


class TbtFeedback(models.Model):
    team_id = models.IntegerField()
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


class TbtMcqMaster(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    mcq_version_id = models.IntegerField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    option_1 = models.CharField(max_length=2048, blank=True, null=True)
    option_2 = models.CharField(max_length=2048, blank=True, null=True)
    option_3 = models.CharField(max_length=2048, blank=True, null=True)
    option_4 = models.CharField(max_length=2048, blank=True, null=True)
    option_5 = models.CharField(max_length=2048, blank=True, null=True)
    correct_option = models.IntegerField(blank=True, null=True)
    answer_explanation = models.CharField(max_length=8192, blank=True, null=True)
    task = models.IntegerField(blank=True, null=True)
    tbt_phase = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_master'


class TbtMcqTask1Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task1_dtls'


class TbtMcqTask2Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task2_dtls'


class TbtMcqTask3Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task3_dtls'


class TbtMcqTask4Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task4_dtls'


class TbtMcqTask5Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task5_dtls'


class TbtMcqTask6Dtls(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    choosen_option = models.CharField(max_length=1024, blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task6_dtls'


class TbtMcqTaskDtls(models.Model):
    task = models.IntegerField()
    team_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    chosen_option = models.IntegerField(blank=True, null=True)
    save_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_mcq_task_dtls'


class TbtSchedule(models.Model):
    task_number = models.IntegerField()
    tasks = models.CharField(max_length=2048, blank=True, null=True)
    launch_date = models.DateTimeField(blank=True, null=True)
    task_deadline = models.DateTimeField(blank=True, null=True)
    absolute_deadline = models.DateTimeField(blank=True, null=True)
    tbt_phase = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_schedule'


class TbtScheduleChallenge(models.Model):
    task_number = models.IntegerField()
    tasks = models.CharField(max_length=2048, blank=True, null=True)
    launch_date = models.DateTimeField(blank=True, null=True)
    task_deadline = models.DateTimeField(blank=True, null=True)
    tbt_phase = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_schedule_challenge'


class TbtStatusChallenge(models.Model):
    team_id = models.IntegerField()
    i_agree_challenge = models.IntegerField()
    task1_arena_uploaded = models.IntegerField()
    task1_arena_upload_time = models.DateTimeField(blank=True, null=True)
    task1_file_name = models.CharField(max_length=64, blank=True, null=True)
    task1_arena_marks = models.FloatField(blank=True, null=True)
    task1_arena_remark = models.CharField(max_length=1024, blank=True, null=True)
    task2_video_uploaded = models.IntegerField()
    task2_video_link = models.CharField(max_length=256, blank=True, null=True)
    task2_video_upload_time = models.DateTimeField(blank=True, null=True)
    task2_code_uploaded = models.IntegerField()
    task2_code_upload_time = models.DateTimeField(blank=True, null=True)
    challenge_task2_total_marks = models.FloatField(blank=True, null=True)
    task2_total_remark = models.CharField(max_length=1024, blank=True, null=True)
    challenge_result = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_status_challenge'


class TbtStatusComplete(models.Model):
    team_id = models.IntegerField()
    task0_noc = models.IntegerField()
    task1_status = models.IntegerField()
    task1_bonus_marks = models.IntegerField(blank=True, null=True)
    task1_total_marks = models.FloatField(blank=True, null=True)
    task1_graded = models.IntegerField()
    task2_status = models.IntegerField()
    task2_bonus_marks = models.IntegerField(blank=True, null=True)
    task2_total_marks = models.FloatField(blank=True, null=True)
    task2_graded = models.IntegerField()
    task3_status = models.IntegerField()
    task3_bonus_marks = models.IntegerField(blank=True, null=True)
    task3_total_marks = models.FloatField(blank=True, null=True)
    task3_graded = models.IntegerField()
    task4_status = models.IntegerField()
    task4_bonus_marks = models.IntegerField(blank=True, null=True)
    task4_total_marks = models.FloatField(blank=True, null=True)
    task4_graded = models.IntegerField()
    task5_status = models.IntegerField()
    task5_bonus_marks = models.IntegerField(blank=True, null=True)
    task5_total_marks = models.FloatField(blank=True, null=True)
    task5_graded = models.IntegerField()
    task6_status = models.IntegerField()
    task6_bonus_marks = models.IntegerField(blank=True, null=True)
    task6_total_marks = models.FloatField(blank=True, null=True)
    task6_graded = models.IntegerField()
    tbt_completed = models.IntegerField()
    award_grade = models.CharField(max_length=64, blank=True, null=True)
    names_ok = models.IntegerField()
    bonus_task_downloaded = models.IntegerField(blank=True, null=True)
    profile_photo_request = models.IntegerField()
    completed_in_days = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_status_complete'


class TbtStatusExperiment(models.Model):
    team_id = models.IntegerField()
    task1_version = models.IntegerField()
    task2_version = models.IntegerField()
    task3_version = models.IntegerField()
    task4_version = models.IntegerField()
    task5_version = models.IntegerField()
    task6_version = models.IntegerField()
    task1_uploaded = models.IntegerField()
    task1_upload_time = models.DateTimeField(blank=True, null=True)
    task1_marks = models.FloatField(blank=True, null=True)
    task1_remark = models.CharField(max_length=1024, blank=True, null=True)
    task2_uploaded = models.IntegerField()
    task2_upload_time = models.DateTimeField(blank=True, null=True)
    task2_marks = models.FloatField(blank=True, null=True)
    task2_remark = models.CharField(max_length=1024, blank=True, null=True)
    task3_uploaded = models.IntegerField()
    task3_upload_time = models.DateTimeField(blank=True, null=True)
    task3_marks = models.FloatField(blank=True, null=True)
    task3_remark = models.CharField(max_length=1024, blank=True, null=True)
    task4_uploaded = models.IntegerField()
    task4_upload_time = models.DateTimeField(blank=True, null=True)
    task4_marks = models.FloatField(blank=True, null=True)
    task4_remark = models.CharField(max_length=1024, blank=True, null=True)
    task5_uploaded = models.IntegerField()
    task5_upload_time = models.DateTimeField(blank=True, null=True)
    task5_marks = models.FloatField(blank=True, null=True)
    task5_remark = models.CharField(max_length=1024, blank=True, null=True)
    task6_uploaded = models.IntegerField()
    task6_upload_time = models.DateTimeField(blank=True, null=True)
    task6_marks = models.FloatField(blank=True, null=True)
    task6_remark = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_status_experiment'


class TbtStatusMcq(models.Model):
    team_id = models.IntegerField()
    task1_mcq_status = models.IntegerField()
    task1_mcq_time = models.DateTimeField(blank=True, null=True)
    task1_mcq_version = models.IntegerField()
    task1_mcq_marks = models.FloatField(blank=True, null=True)
    task2_mcq_status = models.IntegerField()
    task2_mcq_time = models.DateTimeField(blank=True, null=True)
    task2_mcq_version = models.IntegerField()
    task2_mcq_marks = models.FloatField(blank=True, null=True)
    task3_mcq_status = models.IntegerField()
    task3_mcq_time = models.DateTimeField(blank=True, null=True)
    task3_mcq_version = models.IntegerField()
    task3_mcq_marks = models.FloatField(blank=True, null=True)
    task4_mcq_status = models.IntegerField()
    task4_mcq_time = models.DateTimeField(blank=True, null=True)
    task4_mcq_version = models.IntegerField()
    task4_mcq_marks = models.FloatField(blank=True, null=True)
    task5_mcq_status = models.IntegerField()
    task5_mcq_time = models.DateTimeField(blank=True, null=True)
    task5_mcq_version = models.IntegerField()
    task5_mcq_marks = models.FloatField(blank=True, null=True)
    task6_mcq_status = models.IntegerField()
    task6_mcq_time = models.DateTimeField(blank=True, null=True)
    task6_mcq_version = models.IntegerField()
    task6_mcq_marks = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_status_mcq'


class TbtTeachersDtls(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    tbt_clg_id = models.IntegerField()
    team_id = models.IntegerField()
    elsi_tch_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    name_on_cheque = models.CharField(max_length=1024, blank=True, null=True)
    cheque_issued = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=512, blank=True, null=True)
    account_holders_name = models.CharField(max_length=512, blank=True, null=True)
    bank_name = models.CharField(max_length=512, blank=True, null=True)
    bank_address = models.CharField(max_length=512, blank=True, null=True)
    account_type = models.CharField(max_length=512, blank=True, null=True)
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=512, blank=True, null=True)  # Field name made lowercase.
    bankdtl_added_date = models.DateTimeField(blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    alt_email1 = models.CharField(max_length=256, blank=True, null=True)
    alt_email2 = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=50, blank=True, null=True)
    alt_contact2 = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    designation = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    coor_flag = models.IntegerField()
    tbt_flag = models.IntegerField()
    submitted_to_office = models.IntegerField(blank=True, null=True)
    submitted_to_cert_team = models.IntegerField(blank=True, null=True)
    remark = models.CharField(db_column='Remark', max_length=516, blank=True, null=True)  # Field name made lowercase.
    login_created = models.IntegerField()
    profile_photo = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_teachers_dtls'


class TbtTeams(models.Model):
    team_id = models.AutoField(primary_key=True)
    tbt_clg_id = models.IntegerField()
    tbt_phase = models.IntegerField()
    tl_id = models.IntegerField()
    tm1_id = models.IntegerField(blank=True, null=True)
    tm2_id = models.IntegerField(blank=True, null=True)
    tm3_id = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_teams'


class TbtTeamsSchedule(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    launch_date = models.DateTimeField()
    task0_deadline = models.DateTimeField(blank=True, null=True)
    task1_deadline = models.DateTimeField(blank=True, null=True)
    task2_deadline = models.DateTimeField()
    task3_deadline = models.DateTimeField()
    task4_deadline = models.DateTimeField()
    task5_deadline = models.DateTimeField()
    task6_deadline = models.DateTimeField()
    absolute_deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbt_teams_schedule'


class TbtTutorials(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    tutorial_heading = models.CharField(max_length=2048, blank=True, null=True)
    tutorial_video_link = models.CharField(max_length=2048, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbt_tutorials'


class UsersLogin(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=512)
    password = models.CharField(max_length=1024, blank=True, null=True)
    tbt = models.IntegerField()
    active = models.IntegerField()
    agree = models.IntegerField()
    token = models.CharField(max_length=1024, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    change_count = models.IntegerField()
    forgot_count = models.IntegerField()
    remember_token = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_login'
