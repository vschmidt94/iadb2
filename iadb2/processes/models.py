"""
Processes Model(s)

Process app has the functionality for handling organizational processes.
"""
from django.db import models
from django.urls import reverse
from iadb2.base.models import IADBInquiryPageParamType, IADBModel

class Process(IADBModel):
    """
    Process Class

    Defines a Process Area
    """
    name = models.CharField(
        max_length=50,
        verbose_name='Process Name',
        unique=True,
        help_text='Descriptive name for the process area.')
    frequency = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Frequency',
        help_text='''How many times per year the Process should be audited. ( 1 for
                     yearly, 4 for quarterly ).''')
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
        help_text='''Is this Process current in-use. Inactive Processes will NOT be
                     included in audit processing.''')
    note = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Note(s)',
        help_text='''Top-Level for the Process. Generally auditor-to-auditor, for
                     reference only.''')
    iadb1_id = models.PositiveIntegerField(
        default=None,
        null=True,
        verbose_name='IADB1 ID#',
        help_text='UID of Process in iadb1. Used for data migration.')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''Processes define a major internal work process, and also are used
                       to scope individual audits. Audits are conducted on a per-process
                       basis. A single audit will focus on a single process.''',
        inquiry_fields_to_show=['name', 'frequency', 'note', 'is_active'])

    def get_absolute_update_url(self):
        """
        Returns URL to update a process
        """
        return reverse('process_update', args=[str(self.id)])

    class Meta:
        ordering = ['name']
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'

    def __str__(self):
        return self.name


class ProcessComment(IADBModel):
    """
    Process Comment objects
    """
    process = models.ForeignKey(
        'Process',
        verbose_name='For Process',
        on_delete=models.PROTECT,
        related_name='comments')
    comment = models.TextField(
        verbose_name='Comment',
        help_text='''A Comment communicates something auditor-to-auditor about the Process,
                     such as a lesson learned, suggestion, or other such information. There
                     can be multiple comments for a Process.''')

    class Meta:
        ordering = ['process', '-date_created']
        verbose_name = 'Process Comment'
        verbose_name_plural = 'Process Comments'

    def __str__(self):
        return '{}_{}'.format(str(self.process), str(self.id))
