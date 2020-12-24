from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from users.models import StudentProfile,TeacherProfile,Teach


@login_required
def view_list(request):
    if request.user.role == 'STD':
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        class_obj = student_profile.section
        subjects = Teach.objects.filter(Class=class_obj)
        for subject in subjects:
            print(subject.subject.subject_name)
        return render(request, 'marks/subject-list.html', {'subjects': subjects})
    elif request.user.role == 'THR' or request.user.role == 'ADM':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        teaches = Teach.objects.filter(teacher=teacherProfile)
        return render(request, 'marks/subject-list.html', {'teaches': teaches})