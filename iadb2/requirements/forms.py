"""
Requirement App - Forms module
"""

from django import forms
from .models import Document, Requirement, Standard


class DocumentDetailForm(forms.models.ModelForm):
    """
    Document Form

    *Only allows update to notes. Any other update must be via Admin interface.
    """
    doc_identifier = forms.CharField(
        label='Document Identifier',
        disabled=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(
        label='Is Active?',
        disabled=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-control move-left'}))
    doc_title = forms.CharField(
        label='Document Title',
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(
        label='Document Notes',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Document
        fields = ['is_active', 'doc_identifier', 'doc_title', 'note']

    def clean_note(self):
        return self.cleaned_data['note'] or None


class RequirementDetailForm(forms.models.ModelForm):
    """
    Requirement Form

    *Only allows update to notes. Any other update must be via Admin interface.
    """
    identifier = forms.CharField(
        label='Requirement Identifier',
        disabled=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    standard = forms.ModelChoiceField(
        label='From Standard',
        queryset=Standard.objects.all(),
        disabled=True)
    is_active = forms.BooleanField(
        label='Is Active?',
        disabled=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-control move-left'}))
    parent = forms.ModelChoiceField(
        label='Parent',
        queryset=Requirement.objects.all(),
        required=False,
        disabled=True)
    coverage_by = forms.ChoiceField(
        label='Coverage By',
        disabled=True,
        choices=Requirement.COV_CHOICES,
        widget=forms.Select())
    description = forms.CharField(
        label='Description',
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(
        label='Requirement Notes',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Requirement
        fields = ['is_active', 'identifier', 'standard', 'parent',
                  'coverage_by', 'description', 'note']

    def clean_note(self):
        return self.cleaned_data['note'] or None
