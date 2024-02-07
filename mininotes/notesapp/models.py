# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Note(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Note.objects.filter(slug__startswith=original_slug)
        if queryset.exists():
            # If slugs with the same prefix exist, append a unique identifier
            self.slug = f"{original_slug}-{queryset.count() + 1}"
        else:
            self.slug = original_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
