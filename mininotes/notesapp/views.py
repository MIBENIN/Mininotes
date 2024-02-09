from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from . models import Note
from .forms import NoteForm, EditProfileForm
from django.db.models import Q
# from django.db.models.functions import Lower


def homepage(request):
    context = {
        "page_title": "MiniNotes | Home Page"
    }
    return render(request, "index.html", context)


def dashboard(request):
    all_notes = Note.objects.filter(user=request.user)
    print(all_notes)
    query = request.GET.get('search-query')
    if query:
        all_notes = all_notes.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()

    all_notes = all_notes.order_by('-date_created')

    context = {
        "page_title": "MiniNotes | Dashboard",
        "notes": all_notes,
    }
    if not all_notes.exists() and not query:
        context['no_results_message'] = "No notes found."
        context['page_title'] = "MiniNotes | Dashboard - No Notes"
    elif not all_notes.exists() and query:
        context['no_results_message'] = "No search items found."
        context['page_title'] = "MiniNotes | Dashboard - No Search Results"
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
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note Added Successfully.')
            return redirect('noteapp:dashboard')
        else:
            messages.error(request, 'Please correct the form')
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
            messages.success(request, 'Note Edited Successfully.')

            return redirect('noteapp:dashboard')
        else:
            messages.error(request, 'Please correct the form')
    else:
        form = NoteForm(instance=note)

    return render(request, 'editnote.html', {'page_title': "MiniNotes | Edit Note", 'form': form})


def deleteNote(request, slug):
    note = get_object_or_404(Note, slug=slug)

    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note Deleted Successfully.')

        return redirect('noteapp:dashboard')

    return render(request, 'deleteNote.html', {'page_title': "MiniNotes | Delete Note", 'note': note})


def settings(request):
    user = request.user
    context = {
        'page_title': "MiniNotes | Settings",
        'user': user,
    }
    return render(request, 'settings.html', context)


def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('noteapp:settings')
        else:
            messages.error(request, 'Please correct the form')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'page_title': "MiniNotes | Edit Profile",
        "form": form
    }
    return render(request, 'editprofile.html', context)
