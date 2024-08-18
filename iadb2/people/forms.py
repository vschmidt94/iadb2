"""
IADB2 people forms module
"""
from django import forms
from .models import Department, Person

class DepartmentForm(forms.models.ModelForm):
    """
    Add Department form
    """
    dept_name = forms.CharField(
        label='New Department',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter department name'}))
    notes = forms.CharField(
        label='Notes',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Enter notes (if any)'}))

    class Meta:
        model = Department
        fields = ['dept_name', 'notes']


class PersonForm(forms.models.ModelForm):
    """
    Add Person form
    """
    name_first = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'First name'}))
    name_last = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Last name'}))
    email = forms.CharField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'person@company.com'}))
    user_name = forms.CharField(
        label='User ID (Required if Person will become Auditor)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'User ID'}))
    dept = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False)
    is_active = forms.BooleanField(
        label='Is Active?',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))

    class Meta:
        model = Person
        fields = ['name_first', 'name_last', 'email',
                  'user_name', 'dept', 'is_active']
