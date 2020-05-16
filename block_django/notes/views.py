from django.shortcuts import render

from .utils import get_or_create_note


def note_view(request):
    template_name = 'notes/note.html'
    note = get_or_create_note(request)

    return render(request, template_name, {
    })
