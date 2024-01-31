from django.shortcuts import render, get_object_or_404
from . models import Note


def homepage(request):
    context = {
        "page_title": "MiniNotes | Home Page"
    }
    return render(request, "index.html", context)


def dashboard(request):
    notes = Note.objects.all()
    context = {
        "page_title": "MiniNotes | Dashboard",
        "notes": notes,
    }
    return render(request, "dashboard.html", context)


def notedetails(request, slug):
    note = get_object_or_404(Note, slug=slug)
    context = {
        "page_title": "MiniNotes | Note Details",
        "note": note,
    }
    return render(request, 'notedetails.html', context)


def addNote(request):
    return render(request, 'addnote.html')
