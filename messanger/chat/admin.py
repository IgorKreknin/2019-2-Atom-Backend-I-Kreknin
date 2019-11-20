from django.contrib import admin
from chat.models import Chat, Message, Attachment

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
	pass

class MessageAdmin(admin.ModelAdmin):
	pass

class AttachmentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Attachment, AttachmentAdmin)