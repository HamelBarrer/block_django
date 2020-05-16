import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from users.models import User


class Note(models.Model):
    title = models.CharField(max_length=50)
    nota = models.TextField(max_length=300)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


def set_title(sender, instance, *args, **kwargs):
    if instance.title:
        instance.title = instance.title.capitalize()


def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Note.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug


pre_save.connect(set_title, sender=Note)
pre_save.connect(set_slug, sender=Note)
