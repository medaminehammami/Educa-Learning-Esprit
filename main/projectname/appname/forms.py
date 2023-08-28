from django import forms
from .models import Lesson,Topic,Catagory,Contact

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['topic', 'name', 'video_src', 'lesson_src']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'enter your name'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'enter your email'}))
    number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'enter your number'}))
    msg = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'enter your message'}))