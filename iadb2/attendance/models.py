"""
Attendance App - Models Module
"""

import datetime
from django.db import models
from django.utils import timezone
from iadb2.auditors.models import Auditor


class Event(models.Model):
    """
    Event

    Event object will be used to store event/meeting details. This is not
    intended to be a replacement for meeting agendas, minutes, or notes that
    are typically maintained in Jira, etc.  Just a simple record of a
    event/meeting occurance so that users can register their attendance at the
    meeting.

    Attributes:
        date_time (DateTimeField): Event DateTime
        event_type (CharField): Two character id that maps to event type
            choices.
        event_desc (CharField): Event Description (optional)
        duration_min (PositiveIntegerField): Event duration in minutes
        allow_checkin (BooleanField): Allow users to check-in to event?
        checkin_window (PositiveIntegerField): Amount of time before the
            scheduled start and after the scheduled end of the event to allow
            users to check-in.
        notes (TextField): Freeform text field used to make any pertinent
            notes. Not intended as minutes, agenda, etc.
        date_created (DateTimeField): Record creation timestamp.
        created_by_userid: UserID that created the record.
    """
    MONTHLY_AUDITOR_TRAINING = 'MO'
    CANDIDATE_TRAINING = 'CT'
    QUALITY_AMBASSADOR_MEETING = 'QA'
    RCACI_MEETING = 'RC'
    OTHER_EVENT = 'OE'
    EVENT_CHOICES = (
        (MONTHLY_AUDITOR_TRAINING, 'Monthly Auditor Training/Meeting'),
        (CANDIDATE_TRAINING, 'Candidate Training'),
        # (QUALITY_AMBASSADOR_MEETING, 'Quality Ambassador Meeting'),
        # (RCACI_MEETING, 'RCACI Meeting'),
        (OTHER_EVENT, 'Other Event'),
    )
    date_time = models.DateTimeField(
        verbose_name='Event Date-Time')
    event_type = models.CharField(
        max_length=2,
        choices=EVENT_CHOICES,
        default=MONTHLY_AUDITOR_TRAINING)
    event_desc = models.CharField(
        max_length=50,
        verbose_name='Event Description',
        blank='True')
    duration_min = models.PositiveIntegerField(
        default=60,
        verbose_name='Duration (min)',
        blank='True', )
    allow_checkin = models.BooleanField(
        default='True',
        verbose_name='Allow Check-ins')
    checkin_window = models.PositiveIntegerField(
        default=60,
        verbose_name='Check-in Window')
    notes = models.TextField(
        max_length=500,
        blank='True',
        verbose_name='Meeting Notes')
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Added to IADB",
        blank='True')
    created_by_userid = models.CharField(
        max_length=12,
        verbose_name='Created by user',
        blank='True',
        default='Admin')

    def event_verbose(self):
        return dict(Event.EVENT_CHOICES)[self.event_type]

    class Meta:
        ordering = ['-date_time']
        verbose_name_plural = 'Events'

    def __str__(self):
        return '{}-{}'.format(
            str(timezone.localtime(self.date_time)),
            self.event_verbose())


class AttendanceRecord(models.Model):
    """
    Attendance Record Class

    An attendance record is created for any user checking into a event while
    the check-in window is open. (Or manually added by Administrator at any
    time.)

    Attributes:
        attendee (ForeignKey - Auditor):  Auditor attending the event.
        event (ForeignKey - Event): Event that was attended.
        created (DateTimeField): Timestamp of check-in.
        created_by_userid (CharField): User ID that created the record.
    """
    attendee = models.ForeignKey(
        Auditor,
        on_delete=models.PROTECT)
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT)
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Record Created')
    created_by_userid = models.CharField(
        max_length=12,
        verbose_name='Created by user',
        blank='True')

    class Meta:
        ordering = ['-created', 'event']

    def __str__(self):
        return '{} : {}'.format(str(self.event), str(self.attendee))
