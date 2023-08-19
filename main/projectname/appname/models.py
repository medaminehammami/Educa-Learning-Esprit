from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.name

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

