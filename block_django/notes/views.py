from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
    template_name = 'notes/note.html'
    model = Note

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-pk')
