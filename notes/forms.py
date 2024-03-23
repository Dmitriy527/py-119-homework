from django.forms import ModelForm

from notes.models import Notes


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text", "category")