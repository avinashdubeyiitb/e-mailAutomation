# Generated by Django 2.2.12 on 2020-06-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_create_workshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_workshop',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
