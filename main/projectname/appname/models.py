from django.db import models
from register.models import CustomUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.TEACHER)


class Teacher(CustomUser):

    teacher = TeacherManager()

    class Meta:
        proxy = True
    
    def __str__(self):
        return self.username    

class Topic(models.Model):
    name = models.CharField(max_length=100)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.name  


class Lesson(models.Model):   
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video_src = models.CharField(max_length=200)
    lesson_src = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STUDENT)


class Student(CustomUser):

    student = StudentManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username  


class Likes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Comments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment_text = models.TextField()


class EnrolledClasses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)  # Or whatever fields you need

    def __str__(self):
        return f"{self.username} - {self.topic}"


# ... Other models related to the "register" app

#student classes

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def number_likes(self):
        return Likes.objects.filter(student=self.user).count()

    def number_comments(self):
        return Comments.objects.filter(student=self.user).count()

    def number_enrolled_courses(self):
        return EnrolledClasses.objects.filter(student=self.user).count()

    def __str__(self):
        return self.user.username  


#teacher classes
class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def number_topics(self):
        x=0
        x=Topic.objects.filter(teacher=self.user).count()
        return x
    
    def number_lessons(self):
        x = 0
        for topics in Topic.objects.filter(teacher=self.user)  :
            x+=Lesson.objects.filter(topic=topics).count()
        return x 

    def number_likes(self):
        liked=0
        topic_teacher = Topic.objects.filter(teacher=self.user).count()
        lesson_likes =Lesson.objects.filter(topic=topic_teacher)
        liked= Likes.objects.filter(lesson=lesson_likes).count()
        return liked

    def __str__(self):
        return self.user.username 






