from django.db import models

# Create your models here.

class Parts(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10,choices=[('CPU','CPU'),('GPU','GPU')])
    price = models.FloatField()
    release_date = models.IntegerField()
    core_clock = models.FloatField()
    clock_unit = models.CharField(max_length=200)
    TDP = models.IntegerField()
    part_no = models.CharField(max_length=200)
