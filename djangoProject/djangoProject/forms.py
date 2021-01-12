from django import forms

ROLE_CHOICES = [
    ('STD', 'STUDENT'),
    ('THR', 'TEACHER'),
    ('ADM', 'ADMIN'),
    ('OTH', 'OTHERS'),
]


class IssueForm(forms.Form):
    id = forms.CharField(max_length=50, label='Registration number/ employee id',widget=forms.TextInput(attrs={'placeholder': 'Reg Number/Employee Id'}))
    email = forms.EmailField(label='Enter Email address',widget=forms.EmailInput(attrs={'placeholder': 'Enter Email address'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Select your role')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 40,"placeholder":"Explain your issue, so that it is easy for us to help you"}))