from django import forms
from attendance.models import AttendanceLog
from academics.models import SEM_CHOICES


class AttendanceUpdateForm(forms.ModelForm):

    class Meta:
        model = AttendanceLog
        fields = ['absentees', 'conducted_date']

    def __init__(self, *args, **kwargs):
        super(AttendanceUpdateForm, self).__init__(*args, **kwargs)
        self.fields['absentees'].label = "Select all the absentees"
        self.fields['conducted_date'].label = "Class conducted on "


class RequestAttendanceDetails(forms.Form):
    semester = forms.ChoiceField(choices=SEM_CHOICES)

    def __init__(self, *args, **kwargs):
        self.sem = kwargs.pop('semester', None)
        super(RequestAttendanceDetails, self).__init__(*args, **kwargs)
        self.fields['semester'].initial = self.sem
        self.fields['semester'].label = "Select the semester"
