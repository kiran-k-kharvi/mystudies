from django import forms
from django.contrib.auth.models import User
from validPass.models import UserProfileDetails


class myForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileDetails
        fields = ('portfolio_site','profile_pic')