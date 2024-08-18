"""
Document initial populatation script.
"""

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iadb2.settings')

import django
django.setup()

import csv
from iadb2.requirements.models import Document


def populate_documents():
    with open('migration/csv/source_docs.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            d = Document(doc_identifier=row['Doc Num'],
                        doc_title=row['Description'],
                        is_active=True,
                        created_by_userid='admin')
            try:
                d.save()
            except django.db.IntegrityError:
                # skip any already in database
                continue


if __name__ == '__main__':
    print("Populating Documents")
    populate_documents()
