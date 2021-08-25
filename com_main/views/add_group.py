from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from com_main.forms import AddGroupForm
from com_main.models import Group


@method_decorator(login_required, name='dispatch')
class AddGroup(View):
    template_name = 'com_main/add_group.html'
    context = {}

    def get(self, request):
        form = AddGroupForm()
        self.context['form'] = form
        self.context['new'] = True
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        if request.method != 'POST':
            messages.error(request, 'Something went wrong.. Try again')
            return redirect('com_main:add_group')
        members = []
        name_of_group = request.POST.get('name_of_group')
        pks = request.POST.getlist('members')
        new_group = Group.objects.create(name_of_group=name_of_group)
        for pk in pks:
            members.append(User.objects.get(pk=pk))
        new_group.members.set(members)
        new_group.save()
        messages.success(request, f'Group {name_of_group} has been successfully created')
        return redirect('com_main:index')