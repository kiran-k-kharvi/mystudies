from django.db import models
from phone_field import PhoneField
# Create your models here.
class Persons(models.Model):
    ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=40,db_column='First Name Test')
    Last_Name = models.CharField(max_length=40,db_column='Last Name')
    Age = models.IntegerField(help_text='Bvc enter proper Age')
    Email = models.EmailField(unique=True)
    Phone = PhoneField(blank=True,help_text='Contact phone number')
    def __str__(self):
        return self.First_Name+' '+self.Last_Name

