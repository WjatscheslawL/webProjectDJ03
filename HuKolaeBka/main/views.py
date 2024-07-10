from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
        'caption': "Dubai Django"
    }

def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'main/index.html', data)


def new(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/news.html', data)


def history(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/history.html', data)


def about(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/about.html', data)
