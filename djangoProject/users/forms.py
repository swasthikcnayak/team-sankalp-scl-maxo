from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from academics.models import Department, Class, SECTION_CHOICES, SEM_CHOICES
from .models import User, TeacherProfile, StudentProfile


# form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    class Meta:
        model = User
        fields = ['username', 'email', 'role']


# form for user profile update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['date_of_birth'].required = False
        self.fields['last_name'].required = False
        self.fields['image'].required = False
        self.fields['blood_group'].required = False
        self.fields['address_line_1'].required = False
        self.fields['address_line_2'].required = False
        self.fields['address_line_3'].required = False

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'blood_group', 'address_line_1',
                  'address_line_2', 'address_line_3', 'image']


# form for student profile update
class StudentProfileUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    semester = forms.ChoiceField(choices=SEM_CHOICES)
    section = forms.ChoiceField(choices=SECTION_CHOICES)
    cgpa = forms.DecimalField(decimal_places=3)

    def clean_section(self):
        sec = self.cleaned_data.get('section')
        dept = self.cleaned_data.get('department')
        sem = self.cleaned_data.get('semester')
        if Class.objects.filter(semester=sem, section_name=sec, department=dept).count() == 0:
            raise ValidationError("You have entered wrong section either of wrong department or semester")
        return Class.objects.filter(semester=sem, section_name=sec, department=dept).first()

    class Meta:
        model = StudentProfile
        fields = ['department', 'semester', 'section', 'cgpa']


# form for teacher profile update
class TeacherProfileUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    join_date = forms.DateField()

    class Meta:
        model = TeacherProfile
        fields = ['department', 'join_date']
