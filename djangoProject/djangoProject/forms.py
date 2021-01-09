from django import forms

ROLE_CHOICES = [
    ('STD', 'STUDENT'),
    ('THR', 'TEACHER'),
]

class IssueForm(forms.Form):
    id = forms.CharField(max_length=50, label='Registration number/ employee id')
    email = forms.EmailField(label='Enter Email address')
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Select your role')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 40}))

    class Meta:
        widgets = {
            'id': forms.TextInput(attrs={'placeholder': 'Reg Number/Employee Id'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email address'}),
        }

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
