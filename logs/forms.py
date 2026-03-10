from django import forms
from .models import StudySession

class SessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['topic', 'week_number', 'date', 'duration_minutes', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }