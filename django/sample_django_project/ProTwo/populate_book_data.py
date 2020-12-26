import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import Book,BookInfo
from faker import Faker

fakegen = Faker()

language = ['Eng', 'Kan','Hindi','Tamil','Telagu','Marathi']

def add_book():
    test = Book.objects.get_or_create(book_language=random.choice(language),book_Name=fakegen.company())
    print(test)
    b = test[0]
    b.save()
    return b

def populate(N=5):

    for x in range(N):
        book_new = add_book()
        ran = int(random.random()*10)
        for y in range(ran):
            fk_name = fakegen.name()
            fk_url = fakegen.url()
            book_info = BookInfo.objects.get_or_create(book=book_new,name= fk_name,url=fk_url)[0]

if __name__ == '__main__':
    print('Populating Dummy Data') 
    populate(22)
    print('Data Population Done')