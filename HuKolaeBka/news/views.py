from django.shortcuts import render
from .models import MyNews


def home(request):
	return render(request, 'news/news.html')


def news(request):
    newss = MyNews.objects.all()
    return render(request, 'main/news.html', {'newss': newss})
