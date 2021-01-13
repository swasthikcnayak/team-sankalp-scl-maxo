from django import forms
from academics.models import Note


# add new notes to the database
class AddNotesForm(forms.ModelForm):
    class Meta:
        # update the Note model and the required fields
        model = Note
        fields = ['chapter_number', 'chapter_name', 'link']
        # change the widgets
        widgets = {
            'chapter_number': forms.TextInput(attrs={'placeholder': 'Chapter number'}),
            'chapter_name': forms.TextInput(attrs={'placeholder': 'Chapter Name'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddNotesForm, self).__init__(*args, **kwargs)
        # changing the labels
        self.fields['chapter_number'].label = "Enter the chapter number"
        self.fields['chapter_name'].label = "Enter chapter name"
        self.fields['link'].label = "Upload the notes"
