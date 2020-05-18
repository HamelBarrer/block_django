from django.shortcuts import render, redirect
from django.views.generic import View

from .utils import get_or_create_book
from .models import Book

from notes.models import Note
from notes.forms import NoteForm


def book_view(request):
    template_name = 'books/book.html'
    book = get_or_create_book(request)
    quantity = Note.objects.all().count()

    return render(request, template_name, {
        'book': book,
        'quantity': quantity,
    })


def add_book(request):
    template_name = 'books/create_note.html'
    book = get_or_create_book(request)
    form = NoteForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        note = form.save()
        book.notes.add(note.pk)
        return redirect('books:book')
    return render(request, template_name, {
        'form': form,
    })
