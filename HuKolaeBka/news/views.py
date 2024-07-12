from django.shortcuts import render, redirect
from .models import MyNews
from .forms import News_postForm


def home(request):
    return render(request, 'news/news.html')


def news(request):
    newss = MyNews.objects.all()
    return render(request, 'main/news.html', {'newss': newss})


def create_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные были заполнены некорректно"
    form = News_postForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})
