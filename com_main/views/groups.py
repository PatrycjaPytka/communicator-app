from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from com_main.models import Group


@method_decorator(login_required, name='dispatch')
class Groups(View):
    template_name = 'com_main/groups.html'
    context = {}

    def get(self, request):
        self.context['groups'] = Group.objects.all()
        return render(request, self.template_name, self.context)

