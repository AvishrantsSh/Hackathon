from django.db import models
from uuid import uuid4
class Hospital_Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20, default='None')
    address = models.TextField()
    region = models.CharField(default='-', max_length=20)
    country = models.CharField(default='', max_length=20)
    bed_capacity = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    fatalities = models.IntegerField(default=0)

    def __str__(self):
        return self.name
   
class Records(models.Model):
    choice = [
        ("Admitted","Admitted"),
        ("Released","Released"),
        ("Death","Death")
    ]
    age = models.IntegerField()
    medical_history = models.CharField(max_length=50, default='[0,0,0,0,0,0,0]')
    status = models.CharField(max_length=10, choices=choice)

   
    # Create your models here.
