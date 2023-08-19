"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appname import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('playlist/<str:topic_name>/', views.playlist, name='playlist'),
    path('courses/<str:catagory_name>/' , views.courses, name='courses'),
    path('watchvideo/<int:lesson_id>/', views.watchvideo, name='watchvideo'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('teacher_profile/<int:teacher_id>/', views.teacher_profile, name='teacher_profile'),
    path('teachers/', views.teachers, name='teachers'),
    path('update/', views.update, name='update'),
    path('catagories/', views.catagories, name='catagories'),

    
]
