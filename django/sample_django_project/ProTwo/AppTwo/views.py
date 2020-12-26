from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import BookInfo,Book
# Create your views here.

def index(request):
    my_dict = {'my_books' :Book.objects.order_by('book_language')} 
    return render(request,'App_Two_Pages/index.html',context=my_dict)

def secret(request):
    return HttpResponse('<strong>Welcome commando the code is <em>456#90$@3245%2</em> </strong>')
