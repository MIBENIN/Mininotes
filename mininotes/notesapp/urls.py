from django.urls import path
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('note/settings/', views.settings, name="settings"),
    path('note/addnote/', views.addNote, name="addnote"),
    path('note/<slug:slug>/', views.notedetails, name='notedetails'),

]
