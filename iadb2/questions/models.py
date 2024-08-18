"""
Models for Questions  App

Question Models are inherited from a common abstract base 
class. From this common base, questions may exist in one
or more different derived question models:

QuestionMaster Model: 
Contains the master approved question pool

QuestionAudit Model:
Contains Questions that exist on individual audits.

QuestionsReview Model:
Contains Questions that have been submitted for entry
to the Approved Question pool (i.e., the QuestionMaster
model) - but are not yet approved.
"""
import datetime
from django.db import models
from django.utils import timezone

class QuestionAbstract(models.Model):
    """
    Question - Abstract Base Class

    Attributes:

    """
    q_text = models.CharField(max_length=512, blank='False',
                              verbose_name='Question Text')
    q_notes = models.TextField(blank='True', verbose_name='Question Notes')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Added to IADB",
                                        blank='True')
    created_by_userid = models.CharField(max_length=12, verbose_name='Created by user', 
                                         blank='True', default='Admin')

    #TODO: Add requirement trace field

    class Meta:
        abstract = True
    
    def __str__(self):
        id = "Q" + self.id
        return id

class QuestionMaster(QuestionAbstract):
    """
    Question - Master Question Object

    A Master Question is one from which audit questions are cloned.
    An audit will clone (copy) questions out of the Master Question
    pool (this table).  Once the question has been cloned, the master
    and the clone are independent of each other. This allows the 
    master question to be revised, deleted, etc - without impacting
    the question as it exists on the audit.  
    
    Attributes:
        q_status (CharField): Status Code for question.
        q_version (PositiveIntegerField): Version number for this 
            question. The version number should be increased on
            every major revision. 
        q_has_alternates (BooleanField): Has alternate versions.
            Alternate versions all track the parent. This field 
            advises that the question as spawned alternates.
        q_alt_parent (ForeignKey): ID of parent derived from if
            this is an alternate question.
    """
    Q_STATUS_ACTIVE = 'AC'
    Q_STATUS_INACTIVE_SAVE = 'IS'
    Q_STATUS_INACTIVE_PURGE = 'IP'
    Q_STATUS_CHOICES = (
            (Q_STATUS_ACTIVE, 'Active'),
            (Q_STATUS_INACTIVE_SAVE, 'Inactive: Save'),
            (Q_STATUS_INACTIVE_PURGE, 'Inactive: Purge')
            )
    q_status  = models.CharField(max_length=2, choices=Q_STATUS_CHOICES, 
                                    default=Q_STATUS_ACTIVE)
    q_version = models.PositiveIntegerField(default=1, null='FALSE',
                                            verbose_name='Version')





