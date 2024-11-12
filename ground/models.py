from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


# Custom manager to handle custom user models
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Teacher(AbstractBaseUser):
    name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email should be unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name', 'teacher_id']
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} - {self.teacher_id}"


class Student(AbstractBaseUser):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50) 
    email = models.EmailField(unique=True)  
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=128, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['roll_number', 'name'] 

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} - {self.roll_number}"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()


class ClassSession(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_date = models.DateField()
    class_time = models.TimeField()
    total_students = models.IntegerField()
    present_students = models.IntegerField()

    def __str__(self):
        return f"{self.teacher} - {self.class_date} {self.class_time}"


class StudentAttendance(models.Model):
    session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)  
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField()

    class Meta:
        unique_together = ('session', 'student')  

    def __str__(self):
        return f"{self.student} - {'Present' if self.is_present else 'Absent'} on {self.session.class_date}"
