from django import forms
from assignments.models import Assignment, Submission


class AssignmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'start_time', 'end_time', 'maximum_marks', 'description', 'question']
        widgets = {
            'assignment_name': forms.TextInput(attrs={'placeholder': 'Assignment Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Give some description', 'cols': '20', 'rows': '5'}),
            'maximum_marks': forms.NumberInput(attrs={'placeholder': 'Maximum Marks'}),
        }

    def __init__(self, *args, **kwargs):
        super(AssignmentCreationForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['assignment_name'].label = "Assignment name"
        self.fields['description'].label = "Provide some details for student"
        self.fields['maximum_marks'].label = "Maximum marks possible"
        self.fields['start_time'].label = "Assignment starts at"
        self.fields['end_time'].label = "Assignment ends at"
        self.fields['question'].label = "Upload question paper"


class MarksUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student', 'marks_obtained']

    def __init__(self, *args, **kwargs):
        super(MarksUpdateForm, self).__init__(*args, **kwargs)
        self.fields['student'].label = "Select the student"
        self.fields['marks_obtained'].label = "Set the marks"


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['answer']

    def __init__(self, *args, **kwargs):
        super(AssignmentSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].label = "Upload answer script"
