# Generated by Django 3.0.5 on 2020-08-21 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_hospital_records_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_records',
            name='contact',
            field=models.CharField(default='0123456789', max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
