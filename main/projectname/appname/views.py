from django.shortcuts import render, get_object_or_404
from .models import Topic, Lesson, Catagory ,Teacher
from .template_paths import template_paths
from django.urls import reverse
import random

def home(request):
    template_name = 'home'  
    return render(request, template_paths[template_name])

def about(request):
    template_name = 'about'  
    return render(request, template_paths[template_name])

def contact(request):
    template_name = 'contact'  
    return render(request, template_paths[template_name])

def catagories(request):
    catagories = Catagory.objects.all()
    context = {'catagories': catagories}
    template_name = 'catagories'
    return render(request, template_paths[template_name], context)


def courses(request, catagory_name='development'):
    topics = Topic.objects.filter(catagory__name=catagory_name)
    context = {
        'catagory_name': catagory_name,
        'topics': topics,
    }
    template_name = 'courses'  
    return render(request, template_paths[template_name],context)

def playlist(request, topic_name='HTML'):
    lessons = Lesson.objects.filter(topic__name=topic_name)
    context = {
        'topic_name': topic_name,
        'lessons': lessons,
    }
    template_name = 'playlist'  
    return render(request, template_paths[template_name], context)

def watchvideo(request,lesson_id=1):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    context = {
        'lesson': lesson,
    }
    template_name = 'watchvideo'  
    return render(request, template_paths[template_name],context)

def profile(request):
    template_name = 'profile'  
    return render(request, template_paths[template_name])

def login(request):
    template_name = 'login'  
    return render(request, template_paths[template_name])

def register(request):
    template_name = 'register'  
    return render(request, template_paths[template_name])

def teacher_profile(request,teacher_id=1):
    teacher = Teacher.objects.get(pk=teacher_id)
    topics = teacher.topic_set.all()  # Assuming you've set a related name for the ForeignKey in Topic model
    context = {
        'teacher': teacher,
        'topics': topics,
    }
    template_name = 'teacher_profile'  
    return render(request, template_paths[template_name],context)

def teachers(request):
    teachers = Teacher.objects.distinct()  # Retrieve unique teachers
    teacher_data = []
    for teacher in teachers:
        topics = teacher.topic_set.all()
        total_lessons = sum(topic.lesson_set.count() for topic in topics)
        x=0
        likes=str(random.randint(50, 800))
        teacher_data.append({
            'teacher': teacher,
            'total_lessons': total_lessons,
            'likes' : likes
        })

    context = {
        'teacher_data': teacher_data
    }
    template_name = 'teachers'  
    return render(request, template_paths[template_name],context)

def update(request):
    template_name = 'update'  
    return render(request, template_paths[template_name])

