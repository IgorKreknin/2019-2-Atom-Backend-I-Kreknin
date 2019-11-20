from django.db import models
from user.models import User, Member

class Chat(models.Model):
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=48)
    last_message = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.topic

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    chat = models.ForeignKey(Chat, on_delete = models.SET_NULL, null = True)
    content = models.TextField()
    added_at = models.DateTimeField(null = True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Attachment(models.Model):
	#attach_id = models.BigIntegerField()
    chat = models.ForeignKey(Chat, on_delete = models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    message = models.ForeignKey(Message, on_delete = models.SET_NULL, null = True)
    type_of_data = models.CharField(max_length = 20)
    url = models.TextField()

    class Meta:
        verbose_name = 'Прикреплённый файл'
        verbose_name_plural = 'Прикреплённые файлы'
