"""
Requirements App - Models module

Requirements app will encapsulate the modeling needed to
define Standards, Requirements, and Internal Documents.
"""

from django.db import models
from iadb2.base.models import IADBInquiryPageParamType, IADBModel


class Document(IADBModel):
    """
    Documents Class

    Documents are internal ACME Co. Documents such as SOP's, ENGs, etc.
    """

    doc_identifier = models.CharField(
        max_length=20,
        verbose_name='Doc ID',
        unique=True,
        help_text='''ACME Co.'s internal identification number for the
                  Document.''')
    doc_title = models.CharField(
        max_length=128,
        verbose_name='Title',
        help_text='''The Document Title or a brief description.''')
    note = models.TextField(
        blank=True, null=True,
        verbose_name='Note',
        help_text='''(Optional) Auditor-to-Auditor internal note(s) that convey
                     additional information which may be useful or good to
                     know.''')
    is_active = models.BooleanField(
        default=True, verbose_name='Active',
        help_text='''Is the Document considered active or retired?''')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''Documents are internal ACME Co. Documents such as ENGs,
                      SOPs, FRMs, etc. that can relate and provide additional
                      details about a Process. The contents of these Documents
                      define additional requirements that can be considered
                      when TODO... how are we doing this now?''',
        inquiry_fields_to_show=['doc_identifier', 'doc_title', 'note',
                                'is_active'])

    class Meta:
        ordering = ['doc_identifier', ]
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.doc_identifier


class Requirement(IADBModel):
    """
    Requirement Class

    Requirements are defined by Standards. They may also be called 'Clauses'.

    Attributes:
        standard (ForeignKey): Standard the Requirement originates from
        identifier(CharField): Identifier for the Requirement
        description (CharField): Short description of the Requirement
        note (TextField): Additional internal notes, commentary, etc.
        coverage_by (CharField): Two character id that maps to list of
            how/where coverage is obtained.
        parent: (ForeignKey): Points to Parent Requirement
        is_active (BooleanField): Flag if this requirement is active or not.
            Inactive requirements will not be considered in coverage metrics.
        date_created (DateTimeField): Record creation timestamp.
        created_by_userid: UserID that created the record.
    """

    COV_SELF = 'S'
    COV_PARENT = 'P'
    COV_CHILD = 'C'
    COV_NA = 'NA'
    COV_CHOICES = (
        (COV_SELF, 'Self'),
        (COV_PARENT, 'Parent'),
        (COV_CHILD, 'Child(ren)'),
        (COV_NA, 'N/A')
    )

    standard = models.ForeignKey(
        'Standard',
        verbose_name='From Standard',
        on_delete='Protect',
        help_text='''The identifier or name of the Standard this Requirement
                     traces to.''')
    identifier = models.CharField(
        max_length=20,
        verbose_name='Identifier',
        help_text='Requirement identifier.')
    description = models.CharField(
        max_length=100,
        verbose_name='Description',
        help_text='''Brief Description of Requirement. Often the section of the
                     Standard it derives from.''')
    note = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Note',
        null=True,
        help_text='''Auditor-to-Auditor note(s) that convey additional
                     information that may be useful.\nOften explains delegation
                     of coverage.''')
    coverage_by = models.CharField(
        max_length=2,
        choices=COV_CHOICES,
        default=COV_SELF,
        verbose_name='Coverage By',
        help_text='''Covered by. Choices are: SELF = This requirement is a
                     coverage point. PARENT = This requirment inherits the
                     parent's coverage, typically used for standard clauses
                     which end up being long lists and thus don't warrant
                     individual questions.  CHILD(REN) = this requirement
                     delegates coverage to child(ren) requirements.
                     Typically used for 'placeholder' requriements, such as
                     section headers.''')
    parent = models.ForeignKey(
        'self',
        verbose_name='Parent',
        on_delete='Protect',
        blank='True',
        null='True',
        related_name='children',
        help_text='''The Parent requirement (if any) of this requirement. Used
                     in conjunction with COVERAGE (above) to determine coverage
                     obligations.''')
    is_active = models.BooleanField(
        default='True',
        verbose_name='Active',
        help_text='''Is requirement active? Only active Requirements will be
                     considered in coverage logic.''')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=True,
        show_more_link=False,
        about_text='''Requirements are an aspect of a Standard that must be
                      fulfilled in order to be in compliance with that
                      portion of the Standard. Generally, IADB requirements
                      are derived from the "shall" statements in technical
                      Standards. However, requirements are also derived from
                      internal documents - such as SOP's, ENG's, etc. These
                      internal requirements are not typically enumerated
                      within IADB, but should still be considered during an
                      audit.''',
        inquiry_fields_to_show=['standard', 'identifier', 'parent',
                                'coverage_by', 'description', 'note',
                                'is_active'])

    class Meta:
        indexes = [models.Index(fields=['identifier', 'standard']), ]
        ordering = ['identifier', 'standard']
        unique_together = ['standard', 'identifier']
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'

    def __str__(self):
        return '{} § {}'.format(str(self.standard), self.identifier)


class Standard(IADBModel):
    """
    Standard Class

    Defines what standards are being audited to. For example:
    """
    name = models.CharField(
        max_length=20,
        verbose_name='Standard Name',
        help_text='''The name of the Standard, the primary identifier.''')
    revision = models.CharField(
        max_length=5,
        verbose_name='Revision',
        help_text='''Identifier for the exact version of the Standards being
                     used.''')
    is_active = models.BooleanField(
        verbose_name='Is Active',
        help_text='''Is this Standard currently in-use for audit purposes?
                     Inactive Standards will not be included in audit
                      processing.''')
    description = models.CharField(
        max_length=120,
        verbose_name='Description',
        help_text='''The description or title of the Standard. ''')
    date_active = models.DateField(
        verbose_name='Date Active',
        help_text='''Date the Standard was adopted for audit purposes.''')
    date_inactive = models.DateField(
        blank='True',
        null='True',
        verbose_name='Date Retired',
        help_text='''Date the Standard was retired from audit purposes.''')

    # Non-Database attributes
    page_params = IADBInquiryPageParamType(
        show_edit_link=False,
        show_more_link=False,
        about_text='''Standards are formal documents that establish the
                      Requirements that should be followed.''',
        inquiry_fields_to_show=['name', 'revision', 'description',
                                'date_active', 'date_inactive', 'is_active'])

    class Meta:
        ordering = ['name', '-revision', ]
        unique_together = ['name', 'revision']
        verbose_name = 'Standard'
        verbose_name_plural = 'Standards'

    def __str__(self):
        return '{}:{}'.format(self.name, self.revision)
