from django import forms
from attendance.models import AttendanceLog


class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = AttendanceLog
        fields = ['absentees', 'conducted_date']
