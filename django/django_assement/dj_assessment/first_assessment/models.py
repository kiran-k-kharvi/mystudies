from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField(unique=True,null=False)

    def __str__(self):
        return self.first_name+' '+self.last_name
