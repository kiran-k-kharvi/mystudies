from django.shortcuts import render
from datetime import datetime
from myForms import forms
from myForms.models import Persons


# Create your views here.

def index(request):
    t = datetime.now()
    return render(request,'myFormsApp/index.html',context={'time' : t})

def signup(request):
    form = forms.FormSignUp(request.POST or None )
    
    print(request.POST)
    print(request.GET)
    
    print(request.method)

    if request.method == 'POST':
        
        if form.is_valid():
            print(form.cleaned_data)

            print("Got request")
            print("First Name : " + form.cleaned_data['First_Name'])
            print("Last Name : " + form.cleaned_data['Last_Name'])
            print("Age : "+str(form.cleaned_data['Age']))
            print("Email : "+form.cleaned_data['Email'])
            print("Phone : "+str(form.cleaned_data['Phone']))
            new_person = Persons.objects.get_or_create(First_Name= form.cleaned_data['First_Name'],Last_Name=form.cleaned_data['Last_Name'],Age=form.cleaned_data['Age'],Email=form.cleaned_data['Email'],Phone=form.cleaned_data['Phone'])[0]
            new_person.save()
    return render(request,'myFormsApp/signup.html',context={'form':form})