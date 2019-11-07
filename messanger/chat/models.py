from django.db import models
from user.models import User, Member

class Chat(models.Model):
    members = models.ManyToManyField(Member)
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=48)
    last_message = models.TextField()

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    chat = models.ForeignKey(Chat, on_delete = models.SET_NULL, null = True)
    content = models.TextField()
    added_at = models.DateTimeField(null = True)

class Attachment(models.Model):
	#attach_id = models.BigIntegerField()
	chat = models.ForeignKey(Chat, on_delete = models.SET_NULL, null = True)
	user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
	message = models.ForeignKey(Message, on_delete = models.SET_NULL, null = True)
	type_of_data = models.CharField(max_length = 20)
	url = models.TextField()
