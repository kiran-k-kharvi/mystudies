from django.forms import ModelForm
from myForms.models import MyBooks

class MyBooksForm(ModelForm):
    class Meta:
        model = MyBooks
        fields = '__all__'