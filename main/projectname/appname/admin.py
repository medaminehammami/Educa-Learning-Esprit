from django.contrib import admin
from .models import Catagory,Topic,Lesson,Likes, Comments, EnrolledClasses,StudentProfile,TeacherProfile,Student,Teacher,Contact
from register.models import CustomUser

# Register your models here.
admin.site.register(Contact)
admin.site.register(Catagory)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(EnrolledClasses)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Student)
admin.site.register(Teacher)


