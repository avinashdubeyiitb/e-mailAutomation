# Generated by Django 2.2.12 on 2020-06-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200612_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='language',
            field=models.TextField(null=True),
        ),
    ]
