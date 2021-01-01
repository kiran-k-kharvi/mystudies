from django import forms

class FormSignUp(forms.Form):
    First_Name = forms.CharField(max_length=40)
    Last_Name = forms.CharField(max_length=40,)
    Age = forms.IntegerField(help_text='Bvc enter proper Age')
    Email = forms.EmailField()
    Phone = forms.CharField(max_length=10)