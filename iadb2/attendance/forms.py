from django import forms
from .models import Event


class EventForm(forms.models.ModelForm):
    """
    Add Event form
    """
    EVENT_TYPES = (
        ('MO', 'Monthly IA Meeting / Training'),
        ('CT', 'Candidate Training'),
        ('OE', 'Other Event')
    )

    date_time = forms.DateTimeField(label='Event Date and Time (mm/dd/yyyy hh:mm)',
                                              required=True,
                                              widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': '1/15/2018 14:30'}))
    event_type = forms.ChoiceField(label="Event Type",
                                   required=True,
                                   choices=EVENT_TYPES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    event_desc = forms.CharField(label='Event Description',
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Description'}))
    notes = forms.CharField(label='Event Notes',
                                  required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Notes'}))
    allow_checkin = forms.BooleanField(label='Allow Check-ins?',
                                       required=True,
                                       initial=True,
                                       widget=forms.CheckboxInput(attrs={'class': 'form-check-inline'}))
    duration_min = forms.IntegerField(label='Event Duration (minutes)',
                                      required=False,
                                      initial=60,
                                      max_value=480,
                                      min_value=0,
                                      widget=forms.NumberInput(attrs={'class':'form-control'}))
    checkin_window = forms.IntegerField(label='Check-in window (minutes)',
                                        required=False,
                                        initial=60,
                                        max_value=180,
                                        min_value=0,
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['date_time', 'event_desc', 'event_type', 'notes',
                  'duration_min', 'allow_checkin', 'checkin_window']
