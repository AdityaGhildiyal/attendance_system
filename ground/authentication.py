from django.contrib.auth.backends import BaseBackend

from .models import Student, Teacher

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            student = Student.objects.get(email=username)
            
            if student.password == password:  
                return student
            return None
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(id=user_id)
        except Student.DoesNotExist:
            return None

class TeacherEmailAuth(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            
            teacher = Teacher.objects.get(email=username)
            
            if teacher.check_password(password):
                return teacher 
            return None
        except Teacher.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Teacher.objects.get(pk=user_id)
        except Teacher.DoesNotExist:
            return None
