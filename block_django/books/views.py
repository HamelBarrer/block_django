from django.shortcuts import render, redirect

from .utils import get_or_create_book

from notes.models import Note
from notes.forms import NoteForm


def book_view(request):
    template_name = 'books/book.html'
    book = get_or_create_book(request)

    return render(request, template_name, {
        'book': book,
    })


def add_book(request):
    template_name = 'books/create_note.html'
    book = get_or_create_book(request)
    form = NoteForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        note = Note.objects.get(pk=form.pk)
        book.notes.add(note)
        form.save()
        return redirect('books:book')
    return render(request, template_name, {
        'form': form,
    })
