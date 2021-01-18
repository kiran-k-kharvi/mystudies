from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileDetails(models.Model):
    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True,upload_to="myProfilePic")

     