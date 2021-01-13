from django import forms
from attendance.models import AttendanceLog
from academics.models import SEM_CHOICES


# updating the attendance of users
class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        # model and fields
        model = AttendanceLog
        fields = ['absentees', 'conducted_date']

    def __init__(self, *args, **kwargs):
        super(AttendanceUpdateForm, self).__init__(*args, **kwargs)
        # updating the labels
        self.fields['absentees'].label = "Select all the absentees"
        self.fields['conducted_date'].label = "Class conducted on "


# showing details of other semesters
class RequestAttendanceDetails(forms.Form):
    # semester as the input field
    semester = forms.ChoiceField(choices=SEM_CHOICES)

    def __init__(self, *args, **kwargs):
        self.sem = kwargs.pop('semester', None)
        super(RequestAttendanceDetails, self).__init__(*args, **kwargs)
        # update the labels and set the initial content
        self.fields['semester'].initial = self.sem
        self.fields['semester'].label = "Select the semester"
