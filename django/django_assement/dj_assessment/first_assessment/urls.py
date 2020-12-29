from django.urls import path
from first_assessment import views

urlpatterns = [
    path('',views.user,name='USER INFO PAGE'),
]