from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.new, name='news'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history')
]
