from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("noteapp:dashboard")
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()

    return render(request=request, template_name="register.html", context={"form": form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("username:", username)
            print("password:", password)
            if username and password:
                user = authenticate(
                    request, username=username, password=password)

                if user is not None:
                    auth_login(request, user)
                    messages.info(
                        request, f"You are now logged in as {username}.")
                    return redirect("noteapp:dashboard")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(
                    request, "Both username and password are required.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {"page_title": "MiniNotes | Login", "form": form})


def logOut(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("noteapp:homepage")


def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Account deleted successfully")
        logout(request)
        return redirect('noteapp:homepage')
    return render(request, 'deleteAccount.html', {'page_title': 'MiniNotes | Account Deletion'})
