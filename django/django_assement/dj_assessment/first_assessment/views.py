from django.shortcuts import render
from django.http import HttpResponse
from first_assessment.models import User
# Create your views here.
def index(request):
    my_dict = {"intro" :'Welcome to my new project', "nav_to" : 'To check about user details route to "USER/"' }
    return render(request,'first_assess_templates/index.html',context=my_dict)


def user(request):
    my_user = {'User' : User.objects.order_by('id')}
    return render(request,'first_assess_templates/user_info.html',context=my_user)