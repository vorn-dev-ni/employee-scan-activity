# Generated by Django 5.0.3 on 2024-05-16 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0004_checkintype_alter_activityemployees_checkin_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityEmployees',
            new_name='ActivityEmployee',
        ),
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
    ]