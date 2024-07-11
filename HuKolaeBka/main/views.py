from django.shortcuts import render
# from django.http import HttpResponse
from .models import NewsPost

# Create your views here.

data = {
        'caption': "Dubai Django"
    }


def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'main/index.html', data)


def history(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/history.html', data)


def about(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/about.html', data)


def admins(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/admins.html', data)


def news(request):
    newss = NewsPost.objects.all()
    #return render(request, 'main/news.html', {'newss': newss})
    return render(request, 'news/news.html', {'newss': newss})
