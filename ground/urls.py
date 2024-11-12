
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/login/' , views.admin_login , name ="admin.login"),
    path('teacher/login/' , views.teacher_login , name = "teacher.login"),
    path('student/login/' , views.student_login , name = "student.login"),
    path('student/home/' , views.student_home , name="student_home"),
    path('teacher/home/',views.teacher_home , name="teacher_home"),
]





