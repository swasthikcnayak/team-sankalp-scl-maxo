from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from academics.models import Department, Class
from .models import User, TeacherProfile,StudentProfile, SEM_CHOICES


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    class Meta:
        model = User
        fields = ['username', 'email', 'role']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['date_of_birth'].required = False
        self.fields['description'].required = False
        self.fields['last_name'].required = False
        self.fields['image'].required = False

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'description', 'image']


class StudentProfileUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    semester = forms.ChoiceField(choices=SEM_CHOICES)
    section = forms.ModelChoiceField(queryset=Class.objects.all())
    cgpa = forms.DecimalField(decimal_places=3)

    def clean_section(self):
        sec = self.cleaned_data.get('section')
        split = str(sec).split('+')
        if str(self.cleaned_data['department']) != split[0] or str(self.cleaned_data['semester']) != split[1]:
            raise ValidationError("You have entered wrong section either of wrong department or semester")
        return sec

    class Meta:
        model = StudentProfile
        fields = ['department', 'semester', 'section', 'cgpa']


class TeacherProfileUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    join_date = forms.DateField()

    class Meta:
        model = TeacherProfile
        fields = ['department', 'join_date']
