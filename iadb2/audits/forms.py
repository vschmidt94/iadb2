"""
Audits app - Forms
"""

from django import forms
from .models import AuditTemplate, AuditPeriod, AuditHeader
from iadb2.processes.models import Process
from iadb2.requirements.models import Requirement, Document


class AuditTemplateDetailForm(forms.models.ModelForm):
    """
    Audit Template Form

    *Only allows update to notes. Any other update must be via Admin interface.
    """
    for_process = forms.ModelChoiceField(
        label='For Process',
        queryset=Process.objects.all(),
        disabled=True)
    is_active = forms.BooleanField(
        label='Is Active?',
        disabled=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-control move-left'}))
    requirements = forms.ModelMultipleChoiceField(
        label='Requirement(s)',
        queryset=Requirement.objects.all(),
        disabled=True)
    documents = forms.ModelMultipleChoiceField(
        label='Document(s)',
        queryset=Document.objects.all(),
        disabled=True)
    note = forms.CharField(
        label='Audit Template Notes',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = AuditTemplate
        fields = ['for_process', 'is_active', 'requirements', 'documents',
                  'note']

    def clean_notes(self):
        return self.cleaned_data['notes'] or None


class ScheduleAuditForm(forms.models.ModelForm):
    audit = forms.ModelChoiceField(
        queryset=AuditTemplate.objects.all(),
        required=True,
        empty_label=None)
    period = forms.ModelChoiceField(
        queryset=AuditPeriod.objects.all(),
        required=True,
        empty_label=None)

    class Meta:
        model = AuditHeader
        fields = ['audit', 'period']
