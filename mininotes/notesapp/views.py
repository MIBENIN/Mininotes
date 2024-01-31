from django.shortcuts import render, get_object_or_404, redirect
from . models import Note
from .forms import NoteForm


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
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            note = form.save(commit=False)
            # note.user = request.user  # Assuming you have user authentication
            note.save()
            # Redirect to a success page or any other view
            return redirect('noteapp:dashboard')
    else:
        form = NoteForm(initial={'title': request.GET.get('title', ''), 'tags': request.GET.get(
            'tags', ''), 'content': request.GET.get('content', '')})

    return render(request, 'addnote.html', {'page_title': "MiniNotes | Add Note", 'form': form})


def editNote(request, slug):
    note = get_object_or_404(Note, slug=slug)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('noteapp:dashboard')
    else:
        form = NoteForm(instance=note)

    return render(request, 'editnote.html', {'page_title': "MiniNotes | Edit Note", 'form': form})


def deleteNote(request, slug):
    note = get_object_or_404(Note, slug=slug)

    if request.method == 'POST':
        note.delete()
        return redirect('noteapp:dashboard')

    return render(request, 'deleteNote.html', {'page_title': "MiniNotes | Delete Note", 'note': note})


def settings(request):
    return render(request, 'settings.html')
