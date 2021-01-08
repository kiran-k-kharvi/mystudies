from django.db import models
from phone_field import PhoneField
# Create your models here.
class Persons(models.Model):
    ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=40,db_column='First Name Test')
    Last_Name = models.CharField(max_length=40,db_column='Last Name')
    Age = models.IntegerField(help_text='Bvc enter proper Age')
    Email = models.EmailField()
    Phone = PhoneField(blank=True,help_text='Contact phone number')
    def __str__(self):
        return self.First_Name+' '+self.Last_Name+' '+str(self.ID)


class MyBooks(models.Model):
    myList = [('poet','Poetry'),('Philo','Philosopy')]
    MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]
    B_ID = models.AutoField(db_column='Book ID',primary_key=True,)
    Book_Name = models.CharField(db_column='Book Name',max_length=40)
    Book_Type = models.CharField(choices=MEDIA_CHOICES,max_length=10)
    def __str__(self):
        return self.Book_Name + ' ' + self.Book_Type


