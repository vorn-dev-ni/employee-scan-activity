# Generated by Django 5.0.3 on 2024-05-17 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0017_alter_employee_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(default=datetime.datetime(2024, 5, 18, 3, 25, 20, 451301), max_length=200),
        ),
    ]
