from appname.template_paths import template_paths
from .template_path import template_path
from django.shortcuts import render, redirect, get_object_or_404 ,HttpResponseRedirect ,HttpResponse
from django.contrib.auth import authenticate, login, logout as auth_login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()

    template_name = 'register'
    return render(request, template_path[template_name], {'form': form})


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse ("Username or Password is incorrect!")
    else:
        template_name = 'login'
        return render(request, template_path[template_name])



@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = UserChangeForm(instance=request.user)

    template_name = 'update'
    return render(request, template_path[template_name])
