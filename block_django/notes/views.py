from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
    template_name = 'notes/note.html'
    model = Note
