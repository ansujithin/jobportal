import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsProject.settings')
import django
django.setup()

from testApp.models import Jobs
from faker import Faker
fakegen=Faker()

def populate(n):
    for i in range(n):
        fake_loc=fakegen.city()
        fake_title='Project Lead'
        fake_Desc='Responsible to do lead activities'
        fake_sal=10000.0
        jobs_record=Jobs.objects.get_or_create(loc=fake_loc,title=fake_title,Desc=fake_Desc,sal=fake_sal)
populate(100)
