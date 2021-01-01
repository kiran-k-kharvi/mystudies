from django.urls import path
from myForms import views
from django.conf.urls import url

urlpatterns = [
    path('',views.signup,name='signup')
]