"""
Auditors App - Models module
"""
import datetime
from django.db import models
from django.utils import timezone


class AuditorRole(models.Model):
    """
    Auditor Role

    An auditor role serves to define the skill and/or authority of an auditor.

    Attributes:
        role_name (CharField): Descriptive name for the role.
        created (DateTimeField): Record creation timestamp.
        created_by_userid (CharField): Record created by user.h
    """
    role_name = models.CharField(
        max_length=32,
        unique='True')
    created = models.DateTimeField(
        auto_now_add='True',
        verbose_name='Date Added to IADB',
        blank='True')
    created_by_userid = models.CharField(
        max_length=12,
        verbose_name='Created by user',
        blank='True', default='Admin')

    class Meta:
        ordering = ['role_name']
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role_name


class Auditor(models.Model):
    """
    Auditor Class

    Defines Auditor object.
    """
    name_first = models.CharField(
        max_length=40,
        verbose_name='First Name')
    name_last = models.CharField(
        max_length=40,
        verbose_name='Last Name')
    user_id = models.CharField(
        max_length=12,
        verbose_name='User ID')
    email = models.EmailField(
        unique='True')
    is_active = models.BooleanField(
        default='True',
        verbose_name='Is Active')
    roles = models.ManyToManyField(
        AuditorRole,
        verbose_name='Role(s)')
    date_qualified = models.DateField(
        verbose_name='Date Qualified')
    created = models.DateTimeField(
        auto_now_add='True',
        verbose_name='Date Added to IADB',
        blank='True')
    completed_audit_count = models.IntegerField(
        default=0,
        verbose_name='Completed Audit Count')
    is_loto_qualified = models.BooleanField(
        verbose_name='Is LOTO Qualified')
    created_by_userid = models.CharField(
        max_length=12,
        verbose_name='Created by user',
        default='admin')

    class Meta:
        ordering = ['name_last', 'name_first']

    def __str__(self):
        full_name = self.name_first + " " + self.name_last
        return full_name
