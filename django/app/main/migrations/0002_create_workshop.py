# Generated by Django 2.2.12 on 2020-06-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_workshop',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
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
            },
        ),
    ]
