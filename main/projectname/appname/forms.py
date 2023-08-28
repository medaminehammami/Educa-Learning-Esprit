from django import forms
from .models import Lesson,Topic,Catagory

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['topic', 'name', 'video_src', 'lesson_src']