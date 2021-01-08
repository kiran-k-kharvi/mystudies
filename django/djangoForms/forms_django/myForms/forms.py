from django import forms
from django.core import validators

class FormSignUp(forms.Form):
    First_Name = forms.CharField(max_length=40)
    Last_Name = forms.CharField(max_length=40)
    Age = forms.IntegerField(help_text='Bvc enter proper Age')
    Email = forms.EmailField()
    Verify_Email = forms.EmailField()
    Phone = forms.CharField(max_length=10)
    BotCatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        print('*****************************************')
        all_clean_data = super().clean()
        print(all_clean_data)
        print('*****************************************')




        

    # def clean_BotCatcher(self):
    #             if len(self.cleaned_data['BotCatcher']) > 0:
    #                 raise forms.ValidationError("Hi BOT I Got You")
               