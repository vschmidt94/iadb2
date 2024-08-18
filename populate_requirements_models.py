"""
Requirements initial populatation script.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iadb2.settings')

import django
django.setup()

import csv
from iadb2.requirements.models import Standard, Requirement

def populate_standards():
    with open('populating_csv_files/standards.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            std = Standard.objects.get_or_create(name=row['std_name'],
                                                 revision=row['rev'],
                                                 is_active=row['is_active'],
                                                 description=row['desc'],
                                                 date_active=row['date_active'],
                                                 date_inactive=row['date_inactive'])

def populate_requirements():
    with open('migration/csv/requirements.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        std = Standard.objects.filter(name='AS9100', revision='D')

        for row in reader:
            p = row['requirement'].rsplit('.', 1)
            if len(p) == 2:
                theParent = Requirement.objects.filter(identifier=p[0])[0]
            else:
                theParent = None
            


            n = row['comments']
            if n == 'NONE':
                n = None


            req = Requirement(standard=std[0],
                              identifier=row['requirement'],
                              description=row['description'],
                              note=n,
                              parent=theParent,
                              coverage_by=row['coverage_by'],
                              is_active='True',
                              created_by_userid='Admin')
            try:
                req.save()
            except django.db.IntegrityError:
                # skip any already in database
                continue
            
if __name__ == '__main__':
    #print("Populating Standards")
    #populate_standards())

    print("Populating Requirements")
    populate_requirements()