"""
Processes initial populatation script.
"""

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iadb2.settings')

import django
django.setup()

import csv
from iadb2.processes.models import Process


def populate_processess():
    with open('migration/csv/processes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            proc = Process(name=row['Process_Name'],
                           frequency=row['AuditFrequency'],
                           is_active=(row['IsActive'] == 'TRUE'),
                           notes=row['ProcessNotes'],
                           iadb1_id=row['iadb1_id'] )
            try:
                proc.save()
            except django.db.IntegrityError:
                # skip any already in database
                continue


if __name__ == '__main__':
    print("Populating Processes")
    populate_processess()
