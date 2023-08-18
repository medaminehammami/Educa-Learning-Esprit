from django.shortcuts import render
from .template_paths import template_paths

# Create your views here.
def home(request):
    template_name = 'home'  
    return render(request, template_paths[template_name])

def about(request):
    template_name = 'about'  
    return render(request, template_paths[template_name])

def contact(request):
    template_name = 'contact'  
    return render(request, template_paths[template_name])

def courses(request):
    template_name = 'courses'  
    return render(request, template_paths[template_name])

def playlist(request):
    template_name = 'playlist'  
    return render(request, template_paths[template_name])

def watchvideo(request):
    template_name = 'watchvideo'  
    return render(request, template_paths[template_name])

def profile(request):
    template_name = 'profile'  
    return render(request, template_paths[template_name])

def login(request):
    template_name = 'login'  
    return render(request, template_paths[template_name])

def register(request):
    template_name = 'register'  
    return render(request, template_paths[template_name])

def teacher_profile(request):
    template_name = 'teacher_profile'  
    return render(request, template_paths[template_name])

def teachers(request):
    template_name = 'teachers '  
    return render(request, template_paths[template_name])

def update(request):
    template_name = 'update '  
    return render(request, template_paths[template_name])

