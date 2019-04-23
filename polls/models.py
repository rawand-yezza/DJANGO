from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    User_ID=models.BigIntegerField()
    User_name=models.CharField(max_length=15)
    User_Num=models.CharField(max_length=2)
    User_birth= models.DateField()
    User_email=models.EmailField(max_length=25)
    def __str__(self):
        return self.User_name+self.User_Num+self.User_birth
        +self.User_email
class AccessRecord(models.Model):
       
       date= models.DateField()
       def __str__(self):
           return str(self.date)