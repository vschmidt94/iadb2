"""
Auditors initial populatation script.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iadb2.settings')

import django
django.setup()

import csv
from iadb2.auditors.models import Auditor, AuditorRole


def populate_roles():
    with open('populating_csv_files/roles.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            role = AuditorRole.objects.get_or_create( role_name = row[0] )[0]
            role.save()

def populate_auditors():
    with open('populating_csv_files/auditors.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            auditor = Auditor(name_first=row['first_name'],
                              name_last=row['last_name'],
                              user_id=row['user_id'],
                              email=row['email'],
                              date_qualified=row['date_qualified'],
                              completed_audit_count=row['completed_count'],
                              is_loto_qualified=row['is_loto_qualified'] )
            try:
                auditor.save()
            except django.db.IntegrityError:
                # skip any already in database
                continue

            # This is fragile, but should not be needed beyond initial migration
            if row['is_auditor'] == 'True':
                role = AuditorRole.objects.filter(role_name='Auditor').first()
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_qualifying'] == 'True':
                role = AuditorRole.objects.filter(role_name='Qualifying Auditor')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_qa'] == 'True':
                role = AuditorRole.objects.filter(role_name='Quality Ambassador')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_admin'] == 'True':
                role = AuditorRole.objects.filter(role_name='Administrator')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_super_admin'] == 'True':
                role = AuditorRole.objects.filter(role_name='Super Admin')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_support'] == 'True':
                role = AuditorRole.objects.filter(role_name='Support')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_dept_auditor'] == 'True':
                role = AuditorRole.objects.filter(role_name='Departmental Auditor')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)

            if row['is_q_approver'] == 'True':
                role = AuditorRole.objects.filter(role_name='Question Approver')[0]
                print("Assigning %s to role: %s" % (auditor, role) )
                auditor.roles.add(role)


if __name__ == '__main__':
    print("Populating Auditor Roles")
    populate_roles()

    print("Populating Auditors")
    populate_auditors()
