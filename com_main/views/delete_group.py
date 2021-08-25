from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from com_main.forms import DeleteGroupForm
from com_main.models import Group


@method_decorator(login_required, name='dispatch')
class DeleteGroup(View):
    template_name = 'com_main/delete_group.html'
    context = {}

    def get(self, request):
        form = DeleteGroupForm()
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        if request.method != 'POST':
            messages.error(request, 'Something went wrong.. Try again')
            return redirect('com_main:add_group')
        to_delete = request.POST.getlist('groups')
        for pk in to_delete:
            try:
                Group.objects.get(pk=pk).delete()
            except:
                messages.error(request, 'Something went wrong - group does not exist. Try again.')
        messages.success(request, f'Group has been successfully deleted')
        return redirect('com_main:index')