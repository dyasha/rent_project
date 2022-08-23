from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model


ROOM_TYPE_CHOICES = [('P', 'Панельный'),
                     ('K', 'Кирпичный'),
                     ('MK', 'Монолитно-Кирпичный'),
                     ('M', 'Монолитный', )]


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    description = models.TextField(verbose_name='Описание')
    square = models.FloatField(verbose_name='Площадь')
    price = models.IntegerField(verbose_name='Цена')
    room_type = models.CharField(
        verbose_name='Тип Помещения',
        max_length=42,
        choices=ROOM_TYPE_CHOICES
    )
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name='posts')

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.description[:15]
