# Generated by Django 3.0 on 2020-06-19 19:27

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('photo', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AICTE_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.TextField()),
                ('state', models.TextField()),
                ('district', models.TextField()),
                ('city', models.TextField()),
                ('full_address', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
            ],
            options={
                'db_table': 'aicte_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='algo_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo_module_cnt', models.IntegerField()),
                ('will_ttl_wrkshp_cnt', models.IntegerField()),
                ('aval_ttl_wrkshp_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'algo_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='create_workshop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hcn', models.TextField(blank=True, null=True)),
                ('startdate', models.TextField(blank=True, null=True)),
                ('enddate', models.TextField(blank=True, null=True)),
                ('venueadd', models.TextField(blank=True, null=True)),
                ('cooname', models.TextField(blank=True, null=True)),
                ('cooemail', models.EmailField(max_length=254)),
                ('coono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'create_workshop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoDtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro_demo', models.IntegerField()),
                ('i_o_demo', models.IntegerField()),
                ('motor_demo', models.IntegerField()),
                ('pwm_demo', models.IntegerField()),
                ('lcd_demo', models.IntegerField()),
                ('adc_demo', models.IntegerField()),
                ('interrupt_demo', models.IntegerField()),
                ('total_count_demo', models.IntegerField()),
            ],
            options={
                'db_table': 'demo_dtls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ElsiCollegeDtls',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('clg_code', models.TextField(blank=True, null=True)),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('workshop_id', models.IntegerField(blank=True, null=True)),
                ('college_name', models.TextField(blank=True, null=True)),
                ('abbreviation', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('college_type', models.TextField(blank=True, null=True)),
                ('principal_meet', models.IntegerField(blank=True, null=True)),
                ('robots_given', models.IntegerField(blank=True, null=True)),
                ('eyic_allowed', models.TextField(blank=True, null=True)),
                ('eyrtc_allowed', models.IntegerField(blank=True, null=True)),
                ('tbt_allowed', models.IntegerField(blank=True, null=True)),
                ('content_allowed', models.TextField(blank=True, null=True)),
                ('legal_docs', models.TextField(blank=True, null=True)),
                ('legal_docs_remarks', models.TextField(blank=True, null=True)),
                ('loi_status', models.IntegerField(blank=True, null=True)),
                ('loi_format', models.IntegerField(blank=True, null=True)),
                ('loi_remarks', models.TextField(blank=True, null=True)),
                ('po_status', models.TextField(blank=True, null=True)),
                ('po_remark', models.TextField(blank=True, null=True)),
                ('wo_reg', models.TextField(blank=True, null=True)),
                ('wo_invite', models.TextField(blank=True, null=True)),
                ('wo_confirm', models.TextField(blank=True, null=True)),
                ('wo_attend', models.IntegerField(blank=True, null=True)),
                ('hardware_given', models.TextField(blank=True, null=True)),
                ('lab_inaugurated', models.IntegerField(blank=True, null=True)),
                ('phase', models.TextField(blank=True, null=True)),
                ('eys2016_invites', models.TextField(blank=True, null=True)),
                ('team_verify', models.IntegerField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
                ('updated_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'elsi_college_dtls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ElsiTeacherDtls',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('emailid', models.TextField(blank=True, null=True)),
                ('alt_email1', models.TextField(blank=True, null=True)),
                ('alt_email2', models.TextField(blank=True, null=True)),
                ('contact_num', models.TextField(blank=True, null=True)),
                ('alt_contact1', models.TextField(blank=True, null=True)),
                ('department', models.TextField(blank=True, null=True)),
                ('designation', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('coor_flag', models.IntegerField(blank=True, null=True)),
                ('wo_flag', models.IntegerField(blank=True, null=True)),
                ('workshop_id', models.IntegerField(blank=True, null=True)),
                ('wo_attendee', models.IntegerField(blank=True, null=True)),
                ('wo_count', models.IntegerField(blank=True, null=True)),
                ('eyrtc_flag', models.IntegerField(blank=True, null=True)),
                ('tbt_flag', models.IntegerField(blank=True, null=True)),
                ('eyic_flag', models.TextField(blank=True, null=True)),
                ('content_flag', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('status_flag', models.TextField(blank=True, null=True)),
                ('modified_by', models.TextField(blank=True, null=True)),
                ('elsi_flag', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('login_created', models.TextField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
                ('updated_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'elsi_teacher_dtls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='memberdetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('emailid', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, null=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('team', models.CharField(max_length=10, null=True)),
                ('head', models.CharField(max_length=30, null=True)),
                ('cohead', models.CharField(max_length=30, null=True)),
                ('ishead', models.CharField(max_length=10, null=True)),
                ('iscohead', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'member_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ssn_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn_id', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('mail_label', models.CharField(max_length=50)),
                ('rcptmailid', models.CharField(max_length=50)),
                ('delegated_access', models.CharField(max_length=10)),
                ('dcprovider', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ssn_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbtCollegeDtls',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('elsi_clg_id', models.IntegerField(blank=True, null=True)),
                ('region_id', models.TextField(blank=True, null=True)),
                ('college_name', models.TextField(blank=True, null=True)),
                ('abbreviation', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('pincode', models.TextField(blank=True, null=True)),
                ('college_type', models.TextField(blank=True, null=True)),
                ('principal_meet', models.IntegerField(blank=True, null=True)),
                ('robots_given', models.IntegerField(blank=True, null=True)),
                ('tbt_allowed', models.IntegerField(blank=True, null=True)),
                ('tbt_count', models.IntegerField(blank=True, null=True)),
                ('completed', models.IntegerField(blank=True, null=True)),
                ('legal_docs', models.IntegerField(blank=True, null=True)),
                ('legal_docs_remarks', models.TextField(blank=True, null=True)),
                ('loi_status', models.IntegerField(blank=True, null=True)),
                ('po_status', models.TextField(blank=True, null=True)),
                ('po_remark', models.TextField(blank=True, null=True)),
                ('wo_reg', models.TextField(blank=True, null=True)),
                ('wo_invite', models.TextField(blank=True, null=True)),
                ('wo_confirm', models.TextField(blank=True, null=True)),
                ('wo_attend', models.IntegerField(blank=True, null=True)),
                ('phase', models.TextField(blank=True, null=True)),
                ('lab_inaugrated', models.IntegerField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
                ('updated_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbt_college_dtls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkshopDtls',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('active', models.TextField(blank=True, null=True)),
                ('workshop_team', models.TextField(blank=True, null=True)),
                ('start_date', models.TextField(blank=True, null=True)),
                ('end_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workshop_dtls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkshopParticipants',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('workshop_id', models.IntegerField(blank=True, null=True)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('tch_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workshop_participants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkshopsTakenCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('active_member', models.IntegerField()),
                ('preparation_status', models.IntegerField()),
                ('willingness_shown', models.IntegerField()),
                ('total_count', models.IntegerField()),
                ('mumbai_workshop', models.IntegerField()),
                ('non_mumbai_workshop', models.IntegerField()),
                ('total_till_date', models.IntegerField()),
                ('past_year', models.IntegerField()),
                ('past_year_mumbai', models.IntegerField()),
                ('past_year_non_mumbai', models.IntegerField()),
            ],
            options={
                'db_table': 'workshops_taken_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkshopTeamStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_id', models.IntegerField()),
                ('workshop_venue', models.CharField(max_length=100)),
                ('date', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('responder', models.CharField(max_length=50)),
                ('willingness_or_unavailability', models.CharField(blank=True, default='None', max_length=50, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('eYRC', models.CharField(default='0', max_length=50, null=True)),
                ('eYIC', models.CharField(default='0', max_length=50, null=True)),
                ('eYRDC', models.CharField(default='0', max_length=50, null=True)),
                ('eLSI', models.CharField(default='0', max_length=50, null=True)),
                ('web', models.CharField(default='0', max_length=50, null=True)),
                ('course_or_other_eyantra_work', models.CharField(default='0', max_length=50, null=True)),
                ('personal_or_any_other', models.CharField(default='0', max_length=50, null=True)),
                ('approval_eYRC', models.CharField(default='None', max_length=20, null=True)),
                ('approval_eYIC', models.CharField(default='None', max_length=20, null=True)),
                ('approval_eYRDC', models.CharField(default='None', max_length=20, null=True)),
                ('approval_eLSI', models.CharField(default='None', max_length=20, null=True)),
                ('approval_web', models.CharField(default='None', max_length=20, null=True)),
                ('approval_course_or_other_eyantra_work', models.CharField(default='None', max_length=20, null=True)),
                ('approval_personal_or_any_other', models.CharField(default='None', max_length=20, null=True)),
            ],
            options={
                'db_table': 'workshop_team_status',
                'managed': False,
            },
        ),
    ]
