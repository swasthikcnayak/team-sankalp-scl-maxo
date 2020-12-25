from django import forms
from assignments.models import Assignment, Submission


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'start_time', 'end_time', 'maximum_marks', 'question']


class MarksUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student', 'marks_obtained']

    def __init__(self, *args, **kwargs):
        self.assignment_obj = kwargs.pop('assignment_obj', None)
        super(MarksUpdateForm, self).__init__(*args, **kwargs)
        self.student = forms.ModelChoiceField(queryset=Submission.objects.filter(assignment=self.assignment_obj))
