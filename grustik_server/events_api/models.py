from django.db import models
from django.conf import settings
from enum import Enum
from django.shortcuts import get_object_or_404

# Create your models here.

class RoleChoice(Enum):
    """
    Перечисление для поля модели через класс
    """
    ADMIN = 'Администратор'
    MEMBER = 'Участник'
    INVITED = 'Приглашенный'

class EventCategory(Enum):
    """
    Перечисление типов события
    """
    SECRET = 'Закрытое'
    PRIVATE = 'Приватное'
    PUBLIC = 'Открытое'

class Event(models.Model):
    title = models.CharField(verbose_name='Краткое описание события',
                             max_length=255)
    description = models.TextField(verbose_name='Описание события',
                                   blank=True,
                                   null=True)
    category = models.CharField(verbose_name='Категория',
                            max_length=7,
                            choices=[(item.name, item.value) for item in EventCategory])
    location = models.CharField(max_length=255,
                                verbose_name='Место проведения')
    date = models.DateTimeField(verbose_name='Дата и время проведения',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.title + ' ' + self.category

    def get_users(self):
        relations = EventUser.objects.filter(event=self.pk)
        members = map(lambda item: item.user, relations)
        return members

    # def add_user(self, user):
    #     EventUser.objects.create(user=user, event=self)
    #     comment = 'Участник добавлен'
    #     return comment
    #
    # def remove_user(self, user):
    #     event_user = get_object_or_404(EventUser, user=user, event=self)
    #     print('юзер опознан')
    #     event_user.delete()
    #     print('и удален из группы')
    #     comment = 'Участник удален'
    #     return comment


class EventUser(models.Model):
    """
    Модель участника события
    """

    class Meta:
        unique_together = ('user', 'event')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='Роль',
                            max_length=7,
                            choices=[(item.name, item.value) for item in RoleChoice])
    event = models.ForeignKey(Event, related_name='eventusers', on_delete=models.CASCADE)

