from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
	name = models.CharField(max_length = 256)
	login = models.CharField(max_length = 256)
	avatar = models.TextField()
	password = models.CharField(max_length = 32)

class Member(models.Model):
	user = models.OneToOneField(User, on_delete = models.SET_NULL, null = True)
	new_messages = models.TextField()
	last_read_message = models.ForeignKey('chat.Message', on_delete = models.SET_NULL, null = True)
