# Generated by Django 5.0.3 on 2024-05-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0006_employee_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityemployee',
            old_name='time',
            new_name='times',
        ),
    ]
