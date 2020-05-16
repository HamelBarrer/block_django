from .models import Book


def get_or_create_book(request):
    user = request.user
    book_id = request.session.get('book_id')
    book = Book.objects.filter(book_id=book_id).first()
    if book is None:
        book = Book.objects.create(user=user)
    request.session['book_id'] = book.book_id
    return book
