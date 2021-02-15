from django.urls import path
from validPass import views

app_name = 'myValidPass'

urlpatterns = [
    path('',views.register,name='regi'),
    path('login/',views.userLogin,name='myLogin')
]