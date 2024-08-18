"""
People Models

People app has the functionality for handling the base class of a 'person'
A 'person' could be an Auditor, Auditee, or other reference like Process
Owner.
"""
from django.db import models
from django.urls import reverse
from iadb2.base.models import IADBInquiryPageParamType, IADBModel


class Department(IADBModel):
    """
    Department Class

    A look-up table for a Person's assigned department / functional area.

    Not intedend to be anything other than than mildly informative within IADB2. Should
    not be considered authoratatve. Use Outlook contact card when needed.
    """
    dept_name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Department',
        help_text='''A name for the department or process area''')
    note = models.TextField(
        null=True,
        verbose_name='Note',
        help_text='''(Optional) Brief notes or comments about the department.
                     Auditor-to-Auditor.''')

    # Non-Database attribVutes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''Departments TODO - Think department is too narrow for how we use
        this.''',
        inquiry_fields_to_show=['dept_name', 'note',])

    def get_absolute_url(self):
        """
        Returns the url to access a particular department
        """
        return reverse('department_detail', args=[str(self.id)])

    def get_absolute_update_url(self):
        """
        Returns the url to update a particular department
        """
        return reverse('department_update', args=[str(self.id)])

    class Meta:
        ordering = ['dept_name']
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.dept_name


class Person(IADBModel):
    """
    Person Class
    """
    name_first = models.CharField(
        max_length=50,
        verbose_name='First Name',
        help_text='''Person's first name.''')
    name_last = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        help_text='''Person's last name.''')
    email = models.EmailField(
        unique=True,
        help_text='''E-mail address for person.''')
    user_name = models.CharField(
        max_length=50,
        null=True,
        help_text='''(Optional) Acme Co. user name / user id.''')
    dept = models.ForeignKey(
        'Department',
        verbose_name='Department',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='''(Optional) The department / work area for a user.''')
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
        help_text='''Is this an active person record?''')
    iadb1_id = models.PositiveIntegerField(
        default=None,
        null=True,
        verbose_name='IADB1 id')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''TODO''',
        inquiry_fields_to_show=['name_last', 'name_first', 'dept', 'is_active'])

    class Meta:
        ordering = ['name_last', 'name_first']
        verbose_name_plural = 'People'

    def get_absolute_url(self):
        """
        Returns the url to access a particular person
        """
        return reverse('person_detail', args=[str(self.id)])

    def get_absolute_update_url(self):
        """
        Returns the url to update a particular person
        """
        return reverse('person_update', args=[str(self.id)])

    def __str__(self):
        return '{} {}'.format(self.name_first, self.name_last)
