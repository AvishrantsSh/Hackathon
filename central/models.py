from django.db import models
from uuid import uuid4
class Hospital_Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20, default='None')
    address = models.TextField()
    subd = models.CharField(default='-', max_length=20)
    bed_capacity = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    fatalities = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total += 1
        return super(Hospital_Records, self).save(*args, **kwargs)

class Age_Freq(models.Model):
    age = models.IntegerField()
    frequency = models.IntegerField(default=0)


# Create your models here.
