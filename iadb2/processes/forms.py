from django import forms
from .models import Process

class ProcessForm(forms.models.ModelForm):
    """
    Process Form

    *Only allows update to notes. Any other update must be via Admin interface.
    """
    name = forms.CharField(label='Process Name',
                           disabled=True,
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active = forms.BooleanField(label='Is Active?',
                            disabled=True,
                            widget=forms.CheckboxInput(attrs={'class':'form-control move-left' }))
    frequency = forms.IntegerField(label='Frequency',
                            disabled=True,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))
    note = forms.CharField(label='Process Notes',
                           required=False,
                           widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Process
        fields = ['name', 'is_active', 'frequency', 'note']

    def clean_note(self):
        return self.cleaned_data['note'] or None
