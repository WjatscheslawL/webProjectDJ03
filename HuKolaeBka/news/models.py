from django.db import models

class MyNews(models.Model):
    title = models.CharField('Название новости', max_length=50)
    melder = models.CharField('Пользователь', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Moü Новость'
        verbose_name_plural = 'Новости'

