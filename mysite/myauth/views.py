from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest
from .forms import AdvertisementRegister


def my_login(request: WSGIRequest):
    redirect_url = reverse("profile")
    if request.user.is_authenticated:
        return redirect(redirect_url)

    if request.method == "GET":
        return render(request, "myauth/login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("main-page")

    return render(request, "myauth/login.html", {"error": "Пользователь не найден"})


def profile(request: WSGIRequest):
    return render(request, "myauth/profile.html")


def my_logout(request: WSGIRequest):
    redirect_to = reverse("main-page")
    logout(request)
    return redirect(redirect_to)


def my_register(request: WSGIRequest):
    if request.method == 'POST':
        print("POST1")
        form = AdvertisementRegister(request.POST)
        if form.is_valid():
            instance = form.save()

            login(request, instance)
            print("POST2")
            return redirect(
                reverse("main-page")
            )
    else:
        form = AdvertisementRegister()
    context = {
        'form': form
    }
    return render(request, 'myauth/register.html', context)
