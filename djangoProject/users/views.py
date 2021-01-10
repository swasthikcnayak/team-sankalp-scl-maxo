from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from djangoProject.utils import is_student, is_teacher
from .forms import UserRegisterForm, UserUpdateForm, StudentProfileUpdateForm, TeacherProfileUpdateForm
from .models import User, StudentProfile, TeacherProfile


# registering users
@login_required
def register(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'users/register.html')
        elif request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                roleFull = ""
                email = form.cleaned_data.get('email')
                role = form.cleaned_data.get('role')
                user = form.save(commit=False)
                password = User.objects.make_random_password(
                    length=10,
                    allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
                if role == 'ADM':
                    roleFull = 'ADMIN'
                    user.is_staff = True
                    user.is_admin = True
                elif role == 'THR':
                    user.is_staff = True
                    roleFull = 'TEACHER'
                else:
                    roleFull = 'STUDENT'
                """send_mail( 'Login details', 'Here is your login details \n username : ' + username + '\n role : ' + 
                roleFull + '\n password : ' + password, from_email=None, recipient_list=[email], fail_silently=False, ) """
                print(username, roleFull)
                print(password)
                user.set_password(password)
                user.save()
                if role == 'THR':
                    teacher_profile = TeacherProfile.objects.create(user=user)
                    teacher_profile.save()
                elif role == 'STD':
                    student_profile = StudentProfile.objects.create(user=user, cgpa=0.00)
                    student_profile.save()
                messages.success(request,
                                 message="User is registered successfully and an Email has been sent to " + email + ".")
            else:
                messages.add_message(request, messages.ERROR,
                                     message="User is could not be registered check for duplicate username or email")
            return redirect('register')


# profile view
@login_required
def profile(request):
    u_form = None
    p_form = None
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if is_student(request):
            student_profile = StudentProfile.objects.get(user=request.user)
            p_form = StudentProfileUpdateForm(request.POST, instance=student_profile)
        elif is_teacher(request):
            teacher_profile = TeacherProfile.objects.get(user=request.user)
            p_form = TeacherProfileUpdateForm(request.POST, instance=teacher_profile)
        if is_student(request) or is_teacher(request):
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                redirect('profile')
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details")
        else:
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your account has been updated')
                redirect('profile')
    elif request.method == 'GET':
        u_form = UserUpdateForm(instance=request.user)
        if is_student(request):
            student_profile = StudentProfile.objects.get(user=request.user)
            p_form = StudentProfileUpdateForm(instance=student_profile)
        elif is_teacher(request):
            teacher_profile = TeacherProfile.objects.get(user=request.user)
            p_form = TeacherProfileUpdateForm(instance=teacher_profile)
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})
