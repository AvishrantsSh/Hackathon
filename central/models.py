from django.db import models
from uuid import uuid4
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import RegexValidator

class Hospital_Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20, default='None')
    address = models.TextField()
    contact = models.CharField(default='0123456789', max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    region = models.CharField(default='', max_length=20)
    country = models.CharField(default='India', max_length=20)
    bed_capacity = models.CharField(default='0,0,0', max_length=20)
    available = models.CharField(default='0,0,0', max_length=20)
    ctotal = models.IntegerField(default=0)
    crecovered = models.IntegerField(default=0)
    cfatalities = models.IntegerField(default=0)
    ventilator = models.PositiveIntegerField(default=10)
    ppe = models.PositiveIntegerField(default=0)
    blood = models.CharField(default='0,0,0,0,0,0,0,0', max_length=40)

    def __str__(self):
        return self.name
   
class Records(models.Model):
    age = models.IntegerField()
    b_group = models.CharField(default='', max_length=5)
    symptoms = models.CharField(max_length=100, default='[]')
    medical_history = models.CharField(max_length=100, default='[]')

class Inventory_Mng(models.Model):
    uuid = models.UUIDField(default=uuid4)
    choice = [
        ("Pending","Pending"),
        ("Solved","Solved")
    ]
    sender = models.UUIDField()
    date = models.DateField()
    message = models.TextField(max_length=200)
    status = models.CharField(default="Pending", choices=choice, max_length=10)
    def get_absolute_url(self): # new
        return reverse('home')
    
    def __str__(self):
        return str(self.message)[:50]
    # Create your models here.
