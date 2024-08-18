"""
Audits Models

Audits app will encapsulate the modeling needed to define Audit objects
"""

from django.db import models
# from iadb2 import requirements, processesa # TODO - remove if not used.
from iadb2.base.models import IADBInquiryPageParamType, IADBModel


class AuditPeriod(IADBModel):
    """
    AuditPeriod Class

    Defines Audit Periods around the Calendar Year. Mainly used as
    a foreign key by the Audit Class.

    TODO: This is kind of hacky, brute force - revisit
    """
    QUARTER = 'Q'
    CHOICES = ((QUARTER, 'Quarter'),)

    year = models.SmallIntegerField(
        verbose_name='Year',
        default='2018',
        blank=False,
        null=False,
        help_text='''Audit Period Year''')
    type = models.CharField(
        verbose_name='Type',
        max_length=1,
        choices=CHOICES,
        default=QUARTER,
        help_text='''Currently the only available type is Quarter, but
                     could be expanded in future if required.''')
    period = models.SmallIntegerField(
        verbose_name='Period',
        default='1',
        blank=False,
        null=False,
        help_text='''Unique ID of the period within the Year''')
    date_start = models.DateField(
        blank=False,
        verbose_name='Period Start Date',
        help_text='''Date the period begins.''')
    date_end = models.DateField(
        blank=False,
        verbose_name='Period End Date',
        help_text='''Date the period ends.''')

    # IADB2 Control Variables
    # These should exist if planning to use the generic inquiry
    # template / page.

    # Show link ot edit page from inquiry page
    edit_link_on_inquiry_pg = False
    #
    # The "About" verbage that shows on some pages.
    about_text = '''Periods define the calendar periods containin Audits.'''

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=False,
        show_more_link=False,
        about_text='''Audit periods are defined by their start date and stop date.
                      Currently the only type of period available for use is a
                      quarter. Periods are only maintained through the
                      administrative interface.''',
        inquiry_fields_to_show=['year', 'type', 'period', 'date_start',
                                'date_end'])

    class Meta:
        ordering = ['-year', 'period']
        unique_together = ['year', 'period']
        verbose_name = 'Audit Period'
        verbose_name_plural = 'Audit Periods'

    def __str__(self):
        period = str(self.year) + ' ' + self.type + str(self.period)
        return period


class AuditHeader(IADBModel):
    """
    Audit Header class

    Audit Header stores all the top-level details about a specific audit.
    """
    SCHEDULED = 'S'
    IN_PROGRESS = 'IP'
    COMPLETED = 'C'
    STATUS_CHOICES = (
        (SCHEDULED, 'Scheduled'),
        (IN_PROGRESS, 'In-Progress'),
        (COMPLETED, 'Completed'),
    )

    for_process = models.ForeignKey(
        'processes.Process',
        verbose_name='Process To Audit',
        on_delete='Protect',
        related_name='audit_header',
        help_text='''The Process this Audit is defined for.''')
    period_scheduled = models.ForeignKey(
        'audits.AuditPeriod', verbose_name='Period Scheduled',
        on_delete='Protect',
        related_name='period_scheduled',
        help_text='''The period this particular audit is scheduled for.''')
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=SCHEDULED,
        verbose_name='Status',
        help_text='''Audit Status. An audit can be in one of the following
                     states: Scheduled, In-Progress, or Completed.''')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''TODO - see how this page is used.''',
        inquiry_fields_to_show=['for_process', 'period_scheduled', 'status'])

    class Meta:
        ordering = ['-period_scheduled__year', '-period_scheduled__period',
                    'for_process__name']
        unique_together = ['for_process', 'period_scheduled']
        verbose_name = 'Audit'
        verbose_name_plural = 'Audits'

    def __str__(self):
        name = '{} - {}'.format(str(self.for_process),
                                str(self.period_scheduled))
        return name


class AuditTemplate(IADBModel):
    """
    AuditTemplate class

    Defines Audit Templates - which are used as to define how a new
    Audit should be setup.  New Audits essentially begin as copies of some
    particular Audit Template. This allows the Audit Template to be
    changed over time without affecting past Audit Records.
    """
    for_process = models.OneToOneField(
        'processes.Process',
        verbose_name='Process To Audit',
        on_delete='Protect',
        related_name='audit_master_template',
        help_text='''The Process this Audit is defined for.''')
    requirements = models.ManyToManyField(
        'requirements.Requirement',
        verbose_name='Requirement(s)',
        related_name='audit_master_template',
        help_text='''Requirements that this audit should cover.''')
    documents = models.ManyToManyField(
        'requirements.Document',
        verbose_name='Document(s)',
        related_name='audit_templates',
        help_text='''Documents relevant to the Process this audit covers.''')
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Note',
        help_text='''Auditor-to-Auditor internal notes. For reference only.''')
    is_active = models.BooleanField(
        default='True',
        verbose_name='Active',
        help_text='''Is Audit Master Template active? Only active Master
                     Templates will be available for creating Audits''')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''Audit Templates control the initial setup of a new audit.
                      The template defines what Process the audit is for, and
                      what requirements it is designed to cover.  The moment
                      an Audit begins, the Audit Template is used to populate
                      the unique, individual Audit. This allows the Audit
                      Template to be adjusted without breaking past Audits
                      nor will it change currently in-progress audits.''',
        inquiry_fields_to_show=['for_process__name', 'requirements',
                                'documents', 'note', 'is_active'])

    class Meta:
        ordering = ['for_process__name']
        verbose_name = 'Audit Template'
        verbose_name_plural = 'Audit Templates'

    def get_documents(self):
        if self.documents:
            return '%s' % ', '.join(
                [doc.doc_identifier for doc in self.documents.all()])

    def __str__(self):
        template = '{}'.format(str(self.for_process))
        return template

    @staticmethod
    def inquiry_fields():
        """
        Returns is a list of tuples for the fields to show in inquiry view.
        Ordering is important: list order controls ordering of columns in
        inquiry table.
        """
        fields = ['for_process', 'requirements', 'documents', 'note',
                  'is_active']
        l = list()
        for f in fields:
            l.append((f, AuditTemplate._meta.get_field(f).verbose_name,
                      AuditTemplate._meta.get_field(f).help_text))

        return l
