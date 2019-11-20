from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from django import forms

from chat.models import Chat
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from user.models import User, Member


@csrf_exempt
def chat(request, chat_id):
    if request.method == 'GET':
        return JsonResponse({"id": chat_id, "messages": [{"name": "user1", "msg": "blablabla"}, {"name": "user2", "msg": "qweqwe"}, {"name": "user1", "msg": "blablabla"}]})
    return HttpResponseNotAllowed(["GET"])

class NewChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('is_group_chat', 'topic', 'owner')

class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user',)

@csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        members = []
        chatForm = NewChatForm(request.POST)
        membersForm = MembersForm(request.POST)
        if chatForm.is_valid() and membersForm.is_valid():
            current_chat = chatForm.save()
            member = membersForm.save(commit=False)
            member.chat = current_chat
            member.save()
            Member.objects.create(user=current_chat.owner, chat=current_chat, is_creator=True)
    else:
        chatForm = NewChatForm()
        membersForm = MembersForm()
    return render_to_response('new_chat.html', {'chatForm': chatForm, 'membersForm': membersForm},)

@csrf_exempt
def chat_list(request, pk=None):
    if request.method in ('GET'):
        if pk is not None:
        	finded_user = User.objects.all().filter(username=pk)
        	if finded_user is None or len(finded_user) < 1:
        		return JsonResponse({'error': 'user not found'})
        	user = finded_user[0]
        	members = Member.objects.all().filter(user = user.id)
        	chat_list = {}
        	for member in members:
        		chat = member.chat
        		chat_list['chat %s' % chat.id] = {
        			'user_is_creator': member.is_creator,
        			'topic': chat.topic,
        			'is_group_chat': chat.is_group_chat,
        		}
        	return JsonResponse(chat_list)
        return JsonResponse({'error': 'enter user id'})
    return HttpResponseNotAllowed(["GET"])
