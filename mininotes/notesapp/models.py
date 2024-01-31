# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)  # Add a SlugField
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
