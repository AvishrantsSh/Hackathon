# Generated by Django 3.0.5 on 2020-08-21 14:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_Records',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='None', max_length=20)),
                ('address', models.TextField()),
                ('region', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='India', max_length=20)),
                ('bed_capacity', models.CharField(default='0,0,0', max_length=20)),
                ('available', models.CharField(default='0,0,0', max_length=20)),
                ('ctotal', models.IntegerField(default=0)),
                ('crecovered', models.IntegerField(default=0)),
                ('cfatalities', models.IntegerField(default=0)),
                ('ventilator', models.PositiveIntegerField(default=10)),
                ('ppe', models.PositiveIntegerField(default=0)),
                ('blood', models.CharField(default='0,0,0,0,0,0,0,0', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Mng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('sender', models.UUIDField()),
                ('date', models.DateField()),
                ('message', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Solved', 'Solved')], default='Pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('b_group', models.CharField(default='', max_length=5)),
                ('symptoms', models.CharField(default='[]', max_length=100)),
                ('medical_history', models.CharField(default='[]', max_length=100)),
            ],
        ),
    ]
