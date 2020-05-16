from .models import Note


def get_or_create_note(request):
    user = request.user
    note_id = request.session.get('note_id')
    note = Note.objects.filter(note_id=note_id).first()
    if note is None:
        note = Note.objects.create(user=user)
    request.session['note_id'] = note.note_id
    return note
