from django import forms
from assignments.models import Assignment, Submission
from users.models import StudentProfile


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'start_time', 'end_time', 'maximum_marks', 'description','question']


class MarksUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student', 'marks_obtained']


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['answer']
