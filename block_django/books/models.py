import uuid

from django.db import models

from django.db.models.signals import pre_save

from users.models import User

from notes.models import Note


class Book(models.Model):
    book_id = models.CharField(
        max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Note)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_id


def set_book_id(sender, instance, *args, **kwargs):
    if not instance.book_id:
        instance.book_id = str(uuid.uuid4())


pre_save.connect(set_book_id, sender=Book)
