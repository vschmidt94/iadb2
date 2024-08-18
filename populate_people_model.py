"""
People initial populatation script.
"""

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iadb2.settings')

import django
django.setup()

import csv
from iadb2.people.models import Person


def populate_people():
    with open('migration/csv/people.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            p = Person(iadb1_id=row['\ufeffemp_id'],
                        name_first=row['First_Nm'],
                        name_last=row['Last_Nm'],
                        email=row['Email'],
                        user_name=row['CurrentUserName'],
                        is_active=(row['IsActive'] == 'TRUE'),
                        created_by_userid='admin')
            try:
                p.save()
            except django.db.IntegrityError:
                # skip any already in database
                continue


if __name__ == '__main__':
    print("Populating People")
    populate_people()
