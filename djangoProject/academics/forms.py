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
