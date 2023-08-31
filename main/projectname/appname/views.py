from django.shortcuts import render, redirect ,HttpResponseRedirect ,HttpResponse
from register.models import CustomUser
from .models import Topic, Lesson, Catagory,Likes,Comments,EnrolledClasses,TeacherProfile,StudentProfile,Student,Teacher,Contact
from .template_paths import template_paths
from django.urls import reverse
import random
from django.contrib.auth.decorators import login_required
from .forms import LessonForm,ContactForm
from .decorators import teacher_required


def name_teacher(request, teacher_name='Paul'):
    try:
        teacher_profile = TeacherProfile.objects.get(user__username=teacher_name)
        topics = Topic.objects.filter(teacher=teacher_profile.user)
        context = {
            'teacher_profile': teacher_profile,
            'topics': topics,
        }
        template_name = 'name_teacher'
        return render(request, template_paths[template_name], context)
    except Teacher.DoesNotExist:
        return HttpResponse("Teacher not found")


@login_required
def home(request):
    likes_count = Likes.objects.all().count()
    lessons_count = Lesson.objects.all().count()
    topics_count = Topic.objects.all().count()
    if request.method == 'POST':
        try : 
            input_type = request.POST.get('form_type')
            if input_type == 'search_input' :
                search_text = request.POST.get('search_box')
                if  Topic.objects.filter(name=search_text).exists() :
                    playlist_url = reverse('playlist', args=[search_text])
                    return HttpResponseRedirect(playlist_url)
                else :
                    return HttpResponse("Course doesn't exist")
        except Exception as e:
            print(f"An error occurred: {e}")             

    context = {
        'likes_count': likes_count,
        'lessons_count': lessons_count,
        'topics_count' :topics_count
    }
    template_name = 'home'  
    return render(request, template_paths[template_name],context)

def about(request):
    if request.method == 'POST':
        try : 
            input_type = request.POST.get('form_type')
            if input_type == 'search_input' :
                search_text = request.POST.get('search_box')
                if  Topic.objects.filter(name=search_text).exists() :
                    playlist_url = reverse('playlist', args=[search_text])
                    return HttpResponseRedirect(playlist_url)
                else :
                    return HttpResponse("Course doesn't exist")
        except Exception as e:
            print(f"An error occurred: {e}")   
            
    template_name = 'about'  
    return render(request, template_paths[template_name])

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                names=form.cleaned_data['name'],
                emails=form.cleaned_data['email'],
                numbers=form.cleaned_data['number'],
                msgs=form.cleaned_data['msg']
            )
            contact.save()

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    template_name = 'contact'  
    return render(request, template_paths[template_name],context)

def catagories(request):
    if request.method == 'POST':
        try : 
            input_type = request.POST.get('form_type')
            if input_type == 'search_input' :
                search_text = request.POST.get('search_box')
                if  Topic.objects.filter(name=search_text).exists() :
                    playlist_url = reverse('playlist', args=[search_text])
                    return HttpResponseRedirect(playlist_url)
                else :
                    return HttpResponse("Course doesn't exist")
        except Exception as e:
            print(f"An error occurred: {e}")      
    catagories = Catagory.objects.all()
    context = {'catagories': catagories}
    template_name = 'catagories'
    return render(request, template_paths[template_name], context)


def courses(request, catagory_name='development'):
    if request.method == 'POST':
        try : 
            input_type = request.POST.get('form_type')
            if input_type == 'search_input' :
                search_text = request.POST.get('search_box')
                if  Topic.objects.filter(name=search_text).exists() :
                    playlist_url = reverse('playlist', args=[search_text])
                    return HttpResponseRedirect(playlist_url)
                else :
                    return HttpResponse("Course doesn't exist")
        except Exception as e:
            print(f"An error occurred: {e}")      
    topics = Topic.objects.filter(catagory__name=catagory_name)
    context = {
        'catagory_name': catagory_name,
        'topics': topics,
    }
    template_name = 'courses'  
    return render(request, template_paths[template_name],context)

@login_required
def playlist(request, topic_name='HTML'):
    lessons = Lesson.objects.filter(topic__name=topic_name)
    number_lessons = lessons.count()
    if request.method == 'POST':
        input_type = request.POST.get('form_type')
        if input_type == 'search_input' :
            search_text = request.POST.get('search_box')
            if  Topic.objects.filter(name=search_text).exists() :
                playlist_url = reverse('playlist', args=[search_text])
                return HttpResponseRedirect(playlist_url)
        else :
            user = request.user
            if user.role == 'STUDENT':
                enroll_data = {
                'user': user,
                'topic_name': topic_name,
                }
                EnrolledClasses.objects.create(**enroll_data)
            else :
                HttpResponse("You can't because you are a teacher.")

    context = {
        'topic_name': topic_name,
        'lessons': lessons,
        'number_lessons': number_lessons
    }
    template_name = 'playlist'  
    return render(request, template_paths[template_name], context)

@login_required
def watchvideo(request,lesson_id=1):
    lesson = Lesson.objects.get(pk=lesson_id)
    comments = Comments.objects.filter(lesson=lesson)
    comment_user = Comments.objects.filter(student=request.user)
    if request.method == 'POST':
        user = request.user
        
        if user.role == 'STUDENT':
            like_data = {
            'student': user,
            'lesson': lesson,
            }
            try : 
                input_type = request.POST.get('form_type')
                if input_type == 'comment_input' :
                    comment_text = request.POST.get('comment_text')
                    Comments.objects.create(student=user ,lesson=lesson,comment_text=comment_text)   
                elif  input_type == 'like_input' :
                    Likes.objects.create(**like_data)
            except Exception as e:
                print(f"An error occurred: {e}")         
        else :
            return HttpResponse("You can't because you are a teacher.")

    context = {
        'lesson': lesson,
        'comments' : comments,
        'comment_user' : comment_user,
    }
    template_name = 'watchvideo'  
    return render(request, template_paths[template_name],context)

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    if user.role == 'STUDENT':
        return HttpResponseRedirect('/student_profile/')
    elif user.role == 'TEACHER':
        return HttpResponseRedirect('/teacher_profile/')
    

@login_required
def teacher_profile(request):
    # Get the logged-in user's TeacherProfile
    teacher_profile = TeacherProfile.objects.get(user=request.user)
    # Get topics related to the teacher
    topics = Topic.objects.filter(teacher=request.user)
    context = {
        'teacher_profile': teacher_profile,
        'topics': topics,
    }
    template_name = 'teacher_profile'
    return render(request, template_paths[template_name], context)

@login_required
def student_profile(request):
    # Get the logged-in user's StudentProfile
    student_profile = StudentProfile.objects.get(user=request.user)
    # Get enrolled classes related to the student
    enrolled = EnrolledClasses.objects.filter(user=request.user)

    topics = []  # Initialize an empty list to store topics

    for classes in enrolled:
        topics.extend(Topic.objects.filter(name=classes.topic_name))

    context = {
        'student_profile': student_profile,
        'topics': topics,
    }
    template_name = 'student_profile'
    return render(request, template_paths[template_name], context)


def teachers(request):
    teacher_profiles = TeacherProfile.objects.all()  # Retrieve all teacher profiles
    teacher_data = []
    
    for teacher_profile in teacher_profiles:
        teacher = teacher_profile.user # Get the associated Teacher instance
        topics = Topic.objects.filter(teacher=teacher)
        topic = topics.first()
        teacher_data.append({
            'teacher_user': teacher_profile.user.username,
            'teacher_role': teacher_profile.user.role,
            'teacher_topics': teacher_profile.number_topics,
            'teacher_lessons': teacher_profile.number_lessons,
            'topic_name': topic
            })

    context = {
        'teacher_data': teacher_data
    }
    template_name = 'teachers'  
    return render(request, template_paths[template_name], context)

@login_required
@teacher_required
def add_lesson(request):
    template_name = 'add_lesson'  
    if request.method == 'POST':
        form = LessonForm(request.POST)  
        try:
            if form.is_valid():
                lesson = form.save()
                # Redirect to a success page or another view
                return HttpResponseRedirect('/home/')  # Change the URL as needed
        except Exception as e:
            # Print or log the exception for debugging purposes
            print(f"An error occurred: {e}")
            # You can also pass the error message to the template
            context = {'form': form, 'error_message': "An error occurred. Please try again later."}
            return render(request, template_paths[template_name],context)
    else:
        form = LessonForm()  # Replace 'LessonForm' with the actual name of your form class
    
    context = {'form': form}
    
    return render(request, template_paths[template_name],context)



