from appname.template_paths import template_paths
from .template_path import template_path
from django.shortcuts import render, redirect ,HttpResponseRedirect ,HttpResponse
from django.contrib.auth import authenticate ,login  as auth_login 
from django.contrib.auth import logout
from .forms import RegisterForm,UserProfileUpdateForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import CustomUser
from django.apps import apps
from django.db import IntegrityError 

def is_guest(user):
    return not user.is_authenticated
# Create your views here.

@user_passes_test(is_guest, login_url='/home/')
def register(request):
    template_name = 'register'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']  # Assign the selected role
            try:
                user.save()
                # Get the Student and Teacher models using app labels
                Student = apps.get_model('appname', 'Student')
                Teacher = apps.get_model('appname', 'Teacher')
                StudentProfile = apps.get_model('appname', 'StudentProfile')
                TeacherProfile = apps.get_model('appname', 'TeacherProfile')

                if user.role == CustomUser.Role.STUDENT :
                    if Student.objects.filter(username=user.username).count() == 0:
                        student_created = Student.objects.create(username=user.username, email=user.email, password=user.password, role=user.role)
                        StudentProfile.objects.create(user=student_created)
                    else:
                        student_created = Student.objects.get(username=user.username)
                        StudentProfile.objects.create(user=student_created)   

                elif user.role == CustomUser.Role.TEACHER :
                    if Teacher.objects.filter(username=user.username).count() == 0:
                        teacher_created = Teacher.objects.create(username=user.username, email=user.email, password=user.password, role=user.role)
                        TeacherProfile.objects.create(user=teacher_created)
                    else :
                        teacher_created = Teacher.objects.get(username=user.username)
                        TeacherProfile.objects.create(user=teacher_created)
                        
                return HttpResponseRedirect('/login/')
                
            except IntegrityError:
                # Handle duplicate username error
                error_message = "Username is already taken. Please choose a different username."
                return render(request, template_path[template_name], {'form': form, 'error_message': error_message})
            
    else:
        form = RegisterForm()

    return render(request, template_path[template_name], {'form': form})

@user_passes_test(is_guest, login_url='/home/')
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse ("Username or Password is incorrect!")
    else:
        template_name = 'login'
        return render(request, template_path[template_name])


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/') 


@login_required  
def update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else :
        form = UserProfileUpdateForm(instance=request.user)
    context = {'form': form}
    template_name = 'update'
    return render(request, template_path[template_name],context)
