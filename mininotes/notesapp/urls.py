from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('note/addnote/', views.addNote, name="addnote"),
    path('note/edit/<slug:slug>/', views.editNote, name='editnote'),
    path('note/delete/<slug:slug>/', views.deleteNote, name='deletenote'),
    path('note/settings/', views.settings, name="settings"),
    path('note/notedetails/<slug:slug>/',
         views.notedetails, name='notedetails'),
]
