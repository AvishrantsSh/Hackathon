from django.db import models
from uuid import uuid4
class Hospital_Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20, default='None')
    address = models.TextField()
    region = models.CharField(default='', max_length=20)
    country = models.CharField(default='India', max_length=20)
    bed_capacity = models.CharField(default='[0,0,0]', max_length=20)
    available = models.CharField(default='[0,0,0]', max_length=20)
    ctotal = models.IntegerField(default=0)
    crecovered = models.IntegerField(default=0)
    cfatalities = models.IntegerField(default=0)

    def __str__(self):
        return self.name
   
class Records(models.Model):
    choice = [
        ("Admitted","Admitted"),
        ("Released","Released"),
        ("Death","Death")
    ]
    age = models.IntegerField()
    symptoms = models.CharField(max_length=100, default='[]')
    medical_history = models.CharField(max_length=100, default='[]')
    status = models.CharField(max_length=10, choices=choice)

   
    # Create your models here.
