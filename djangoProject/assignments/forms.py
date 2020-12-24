from django import forms
from assignments.models import Assignment


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'start_time','end_time','maximum_marks','question']
