from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from com_main.forms import FindGroupform


@method_decorator(login_required, name='dispatch')
class Index(View):
    template_name = 'com_main/index.html'
    context = {}

    def get(self, request):
        self.context['form'] = FindGroupform()
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.method != 'POST':
            messages.error(request, 'Something went wrong.')
        group_name = request.POST.get('name_of_group')
        messages.success(request, f'Chosen group {group_name}')
        return redirect('com_main:index')