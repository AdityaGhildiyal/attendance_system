from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student,Teacher  
from .forms import StudentLoginForm , TeacherLoginForm
from .authentication import EmailAuthBackend,TeacherEmailAuth

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:  
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('admin_dashboard')  
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'admin_login.html')

def teacher_login(request):
    
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password=form.cleaned_data['password']

            try:
                teacher = authenticate(request , username=email , password=password)

                if teacher is not None:
                    login(request , teacher ,backend=TeacherEmailAuth)
                    return redirect('teacher_home')
                else:
                   messages.error(request , 'User does not exist')
            except Teacher.DoesNotExist:
                messages.error(request,'Invalid email or password')
    
    else:
        form=TeacherLoginForm()

    return render(request, 'teacher_login.html' , {'form' : form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='/student/login/')  
def student_home(request):
    return render(request, 'student_home.html')


@login_required(login_url='/teacher/login/')  
def teacher_home(request):
    return render(request, 'teacher_home.html')


def teacher_home(request):
    return render(request,'teacher_home.html')

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                
                student = authenticate(request, username=email, password=password)
                
                if student is not None:
                    login(request, student,backend=EmailAuthBackend)
                    return redirect('student_home')  
                else:
                    messages.error(request, 'Invalid email or password for student')
            except Student.DoesNotExist:
                messages.error(request, "User doesn't exist")

    else:
        form = StudentLoginForm()

    return render(request, 'student_login.html', {'form': form})
                
