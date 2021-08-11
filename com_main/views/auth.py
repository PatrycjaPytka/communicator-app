from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserForm


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('com_main:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], 
                                            password=form.cleaned_data['password1'],
                                            )           
            user.save()
            return redirect('com_main:index')

        else:
            return redirect('com_main:sign_up')

    else:
        form = UserCreationForm()

    return render(request, 'com_main/sign_up.html', {
                'form':form,
                })


def log_in(request):
    if request.user.is_authenticated:
        return redirect('com_main:index')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password'],
                                )
            if user:
                login(request, user)
                return redirect('com_main:index')
    form = UserForm()
    return render(request, 'com_main/login.html', {
                'form': form,
                })


@login_required
def log_out(request):
    logout(request)
    return redirect('com_main:log_in')


