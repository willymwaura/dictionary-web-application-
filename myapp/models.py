
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Feature (models.Model):
    name=models.CharField(max_length=10)
    date=models.DateTimeField(default=now,blank=True)



