# Generated by Django 2.2.12 on 2020-05-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tbtcollegedtls'),
    ]

    operations = [
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
    ]
