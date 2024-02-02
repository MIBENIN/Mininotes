from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout", views.logOut, name="logout"),
]
