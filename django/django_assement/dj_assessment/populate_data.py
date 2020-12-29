import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dj_assessment.settings')

import django
django.setup()

from first_assessment.models import User
from faker import Faker
import random

fakergen = Faker()

def populate(no_of_records):
    for x in range(no_of_records):
        fk_age = int(random.random()*100)
        fk_fname = fakergen.first_name()
        fk_lname = fakergen.last_name()
        fk_email = fakergen.unique.ascii_free_email()
        us = User.objects.get_or_create(first_name=fk_fname,last_name=fk_lname,age=fk_age,email=fk_email)
        print(us)
        us = us[0]
        us.save()

if __name__ == '__main__':
    print('populating the user data')
    populate(10)
    print('user data population done')

