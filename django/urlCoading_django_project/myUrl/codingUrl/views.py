from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'my_templates/index.html')

def other(request):
    c = {"mydesc" : "hi kiran whatsssuuuppppp man"}
    return render(request,'my_templates/other.html',context=c)

def relative_url_temp(request):
    return render(request,'my_templates/relative_url_template.html')