from django.forms import ModelForm

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = (
            'title', 'nota'
        )
        labels = {
            'title': 'Titulo',
            'nota': 'Nota',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-input',
        })
        self.fields['nota'].widget.attrs.update({
            'class': 'form-input',
        })
