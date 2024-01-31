# admin.py

from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    # Customize the displayed columns in the admin list view
    list_display = ('title', 'user', 'date_created', 'date_modified')
    # Enable searching by title and content
    search_fields = ('title', 'content')
    # Automatically populate the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Note, NoteAdmin)
