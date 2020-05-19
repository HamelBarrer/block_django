from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'nota')
    list_display = ('__str__', 'user', 'slug', 'created_at')


admin.site.register(Note, NoteAdmin)
