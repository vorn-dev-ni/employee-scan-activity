# Generated by Django 5.0.3 on 2024-05-17 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0010_alter_activityemployee_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityemployee',
            name='type',
        ),
    ]