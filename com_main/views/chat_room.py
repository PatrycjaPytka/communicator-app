from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from com_main.models import Group


@method_decorator(login_required, name='dispatch')
class ChatRoom(View):
    template_name = 'com_main/chat_room.html'
    context = {}

    def get(self, request, room_name):
        group = Group.objects.get(name_of_group=room_name)
        self.context['groups'] = Group.objects.all()
        self.context['group'] = group
        return render(request, self.template_name, self.context)