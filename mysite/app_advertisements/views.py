from django.http import HttpResponse
from django.shortcuts import render, redirect  # перенаправление
from django.urls import reverse  # для получения ссылки по названию в параметре name
from .models import Advertisement
from .forms import AdvertisementForm
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        "advertisements": advertisements
    }
    return render(request, "index.html", context)

def post_adv(request: WSGIRequest):

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)  # передаём в форму
        if form.is_valid(): # валидируем
            adv = Advertisement(**form.cleaned_data)  # добавляем в БД
            adv.user = request.user # узнаём пользователя по запросу
            adv.save()  # сохранил запись
            return redirect(  # переадресция на главную страницу
                reverse("main-page")
            )
    else:
        form = AdvertisementForm()
    context = {
        "form": form
    }
    return render(request, "advertisement-post.html", context)

def top_sellers(request):
    return render(request, 'top-sellers.html')