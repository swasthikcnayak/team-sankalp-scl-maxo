from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from academics.models import Class
from assignments.models import Submission
from users.models import StudentProfile, TeacherProfile, Teach
from djangoProject.utils import is_student, is_teacher, is_admin


# view list of subjects taken by student and list of teaching subject by teacher
@login_required
def view_list(request):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        subjects = Teach.objects.filter(Class=student_profile.section)
        return render(request, 'marks/subject-list.html', {'subjects': subjects})
    elif is_teacher(request):
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'marks/subject-list.html', {'teaches': teaches})


# display student list for teacher
@login_required
def students_list(request, subjectId, classId):
    if is_teacher(request):
        class_obj = get_object_or_404(Class, id=classId)
        students_this_section = StudentProfile.objects.filter(section=class_obj)
        return render(request, 'marks/student-list.html', {'students': students_this_section, 'subjectId': subjectId})


# get details of marks of that particular student for teacher
@login_required
def student_marks_detail(request, classId, subjectId, studentId):
    if is_teacher(request):
        student_profile = get_object_or_404(StudentProfile, id=studentId)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject__id=subjectId)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})


# get details of the the current logged in students marks of that subject
@login_required
def marks_detail(request, subjectId):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject__id=subjectId)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})
