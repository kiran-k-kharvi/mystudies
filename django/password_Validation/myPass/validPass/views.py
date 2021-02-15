from django.shortcuts import render
from validPass.forms import myForm,UserProfileForm


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request,'myTemp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Hi bvs")

    

def register(request):
    registered = False
    if request.method == 'POST':
    
        userDetails =  myForm(data=request.POST)
        print("userDetails : ",userDetails,end="")
        
        portfolioDetails = UserProfileForm(data=request.POST)
        print("portfolioDetails : " , portfolioDetails,end="")
        

        if userDetails.is_valid() and portfolioDetails.is_valid():
            
            newUser = userDetails.save()
            print("newUser : ",newUser,end="")
            newUser.set_password(newUser.password)
            newUser.save()
            
            profile = portfolioDetails.save(commit=False)
            profile.user = newUser
           
            print("profile : " , type(profile),end="")

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()
            print()
            print()
            print()
            print("profile : " , profile,end="")

            registered = True
        
        else:
            print(userDetails.errors,portfolioDetails.errors)
         
    else:
        userDetails = myForm()
        portfolioDetails = UserProfileForm()

    return render(request,'myTemp/registration.html',
                                                context={
                                                'regForm' :userDetails,
                                                'ppForm':portfolioDetails,
                                                'registered':registered
                                                })

    
def userLogin(request):

    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        user = authenticate(username=userName,password=passWord)
        print()
        print(user)
        print()
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("gone gone ")
            return HttpResponse("invalid user name : {} and password : {}".format(userName,passWord))
    else:
        return render(request,'myTemp/login.html',{})

