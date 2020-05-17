from django.shortcuts import render, redirect

from .forms import NoteForm


# def note_view(request):
#     template_name = 'notes/create_note.html'
#     form = NoteForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         print(form)
#         form.save()
#         return redirect('home:index')

#     return render(request, template_name, {
#         'form': form,
#     })
