'''
Base Models

The base module should only contain common, shared defnintions and support.
'''

from collections import namedtuple
from django.db import models

# Named tuple type for inquiry page parameters
# IADB models that are going to make use of the generic-ized IADB list view need to
# provide these values
IADBInquiryPageParamType = namedtuple(
    'iadb_page_params', ['show_edit_link', 'show_more_link', 'about_text', 'inquiry_fields_to_show'])


class IADBModel(models.Model):
    '''
    Abstract base class for IADB2 data models.

    Adds a common inquiry_fields() function.
    '''

    # Common database attributes for every table implemented from IADBModel
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date Created`')
    created_by_userid = models.CharField(
        max_length=12,
        default='iadb_sys',
        verbose_name='Created By')

    class Meta:
        abstract = True

    @classmethod
    def inquiry_fields(cls):
        """
        Returns a list of tuples for the fields to show in the inquiry view.
        Ordering is important: list order controls ordering of columns in inquiry table.
        """
        field_list = list()

        try:
            cls.page_params.inquiry_fields_to_show
        except NameError:
            raise NameError("Model instance has not defined help_fields attribute.")
        else:
            for field in cls.page_params.inquiry_fields_to_show:
                field_list.append((field, cls._meta.get_field(field).verbose_name,
                                   cls._meta.get_field(field).help_text))

        return field_list
