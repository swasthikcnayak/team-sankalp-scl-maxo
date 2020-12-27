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
        self.assignment_id = kwargs.pop('assignment_id', None)
        super(MarksUpdateForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Submission.objects.filter(assignment__id=self.assignment_id).values_list(
            'student__user__username', flat=True)


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['answer']
