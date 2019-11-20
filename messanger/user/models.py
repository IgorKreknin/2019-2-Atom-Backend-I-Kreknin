from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
        avatar = models.TextField(null = True, default = "http://example.com/img")

        class Meta:
            ordering = ('date_joined',)
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'

        def toJSONResponse(self):
            return ({"username": self.username, "first_name": self.first_name, "last_name": self.last_name, "is_active": self.is_active})

        def __str__(self):
            return '%s (%s %s)' % (self.username, self.first_name, self.last_name)

class Member(models.Model):
        user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
        chat = models.ForeignKey('chat.Chat', on_delete = models.SET_NULL, null = True)
        new_messages = models.TextField()
        last_read_message = models.ForeignKey('chat.Message', on_delete = models.SET_NULL, null = True)
        is_creator = models.BooleanField(default = False)

        class Meta:
            verbose_name = 'Участник чата'
            verbose_name_plural = 'Участники чата'

        def __str__(self):
            return '%s (чат "%s")' % (self.user.username, self.chat.topic)
