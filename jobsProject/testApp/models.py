from django.db import models

# Create your models here.
class Jobs(models.Model):
    loc=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    Desc=models.CharField(max_length=100)
    sal=models.FloatField()
