import json

from django.shortcuts import render
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
    template_name = 'notes/note.html'
    model = Note

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-pk')


def graphic(request):
    note = Note.objects.filter(user=request.user).order_by('-pk')

    return render(request, 'notes/graphic.html', {
        'note': note,
    })
