from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, StudentProfileUpdateForm, TeacherProfileUpdateForm
from django.http import HttpResponse
from .models import User, StudentProfile, TeacherProfile
from academics.models import Department

@login_required
def register(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            roleFull = ""
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
            send_mail(
                'Login details',
                'Here is your login details \n username : ' + username + '\n role : ' + roleFull + '\n password : ' + password,
                from_email=None,
                recipient_list=[email],
                fail_silently=False,
            )
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
            return redirect('register')
        else:
            messages.add_message(request, messages.ERROR,
                                 message="User is could not be registered check for duplicate username or emails")
    else:
        form = UserRegisterForm()
    return render(request, 'users/password_reset.html', {'form': form})


@login_required
def profile(request):
    department = Department.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if request.user.role == 'STD':
            student_profile = StudentProfile.objects.get(user=request.user)
            p_form = StudentProfileUpdateForm(request.POST, instance=student_profile)
        elif request.user.role == 'THR':
            teacher_profile = TeacherProfile.objects.get(user=request.user)
            p_form = TeacherProfileUpdateForm(request.POST, instance=teacher_profile)
        else:
            p_form = None
        if request.user.role == 'STD' or request.user.role == 'THR':
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                print("saved")
                messages.success(request, f'Your account has been updated!')
                redirect('profile')
        else:
            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your account has been updated')
                redirect('profile')
            messages.add_message(request,messages.ERROR,'Please enter all the required fields correctly')
    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.role == 'STD':
            student_profile = StudentProfile.objects.get(user=request.user)
            p_form = StudentProfileUpdateForm(instance=student_profile)
        elif request.user.role == 'THR':
            teacher_profile = TeacherProfile.objects.get(user=request.user)
            p_form = TeacherProfileUpdateForm(instance=teacher_profile)
        else:
            p_form = None
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form,'title':'PROFILE'})
