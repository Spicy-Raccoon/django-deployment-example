import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","pro_two.settings")

import django
django.setup()

#Fake population script

import random
from app_two.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):

        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.ascii_free_email()

        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Population complete")
