from django.contrib import admin

# Register your models here.

from .models import Student,Teacher,StudentAttendance,ClassSession

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentAttendance)
admin.site.register(ClassSession)


#name = aditya 