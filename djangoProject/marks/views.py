from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from academics.models import Class, Subject
from assignments.models import Submission
from users.models import StudentProfile, TeacherProfile, Teach


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


@login_required
def students_list(request, classId, subjectId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        class_obj = Class.objects.get(id=classId)
        students_this_section = StudentProfile.objects.filter(section=class_obj)
        return render(request, 'marks/student-list.html', {'students': students_this_section,'subjectId':subjectId})

@login_required
def student_marks_detail(request, classId, subjectId,studentId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        student_profile = StudentProfile.objects.filter(id=studentId).first()
        subject = Subject.objects.get(id=subjectId)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject=subject)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})


@login_required
def marks_detail(request, subjectId):
    if request.user.role == 'STD':
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        subject = Subject.objects.get(id=subjectId)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject=subject)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})
