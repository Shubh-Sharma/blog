from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def profile_view(request):
    context = {
        "title": request.user.username
    }
    return render(request, "profile.html", context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get("next")
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "title": "login",
        "form": form
    }
    return render(request, "form.html", context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    next = request.GET.get("next")
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "title": "register",
        "form": form
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")