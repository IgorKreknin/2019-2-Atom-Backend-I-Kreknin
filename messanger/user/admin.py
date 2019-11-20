from django.contrib import admin
from user.models import User, Member
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	pass

class MemberAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)