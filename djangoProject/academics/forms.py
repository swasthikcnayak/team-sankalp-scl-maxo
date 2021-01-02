from django import forms
from academics.models import Note


class AddNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['chapter_number', 'chapter_name', 'link']

        widgets = {
            'chapter_number': forms.TextInput(attrs={'placeholder': 'Chapter number'}),
            'chapter_name': forms.TextInput(attrs={'placeholder': 'Chapter Name'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddNotesForm, self).__init__(*args, **kwargs)
        self.fields['chapter_number'].label = "Enter the chapter number"
        self.fields['chapter_name'].label = "Enter chapter name"
        self.fields['link'].label = "Upload the notes"
