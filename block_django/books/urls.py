from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.book_view, name='book'),
    path('crear_nota', views.add_book, name='add_note'),
]
