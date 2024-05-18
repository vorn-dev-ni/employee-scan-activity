# Generated by Django 5.0.3 on 2024-05-16 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0002_remove_employees_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyOutlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('provinces', models.CharField(max_length=255)),
                ('lati', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityEmployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('time', models.TimeField()),
                ('checkin_type', models.CharField(max_length=25)),
                ('duration', models.FloatField(default=0)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='scan.employees')),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='scan.companyoutlet')),
            ],
        ),
    ]
