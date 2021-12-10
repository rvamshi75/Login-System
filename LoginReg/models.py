from django.db import models

# Create your models here.
class Reg(models.Model):
    user=models.CharField(max_length=30,primary_key=True)
    pwd=models.CharField(max_length=10)
