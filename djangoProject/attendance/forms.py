from django import forms
from attendance.models import AttendanceLog
from users.models import StudentProfile


class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = AttendanceLog
        fields = ['absentees', 'conducted_date']

    def __init__(self, *args, **kwargs):
        self.class_obj = kwargs.pop('class_obj', None)
        super(AttendanceUpdateForm, self).__init__(*args, **kwargs)
        self.absentees = forms.ModelMultipleChoiceField(queryset=StudentProfile.objects.filter(section=self.class_obj))