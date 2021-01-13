from django.urls import path
from codingUrl import views

#template tagging
app_name = 'kiran'

urlpatterns = [
    path('url',views.relative_url_temp,name='relative'),
    path('other',views.other,name='other'),

]