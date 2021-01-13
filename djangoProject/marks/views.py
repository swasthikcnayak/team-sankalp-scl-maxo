from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from academics.models import Class
from assignments.models import Submission
from djangoProject.utils import is_student, is_teacher
from users.models import StudentProfile, Teach


# view list of subjects taken by student and list of teaching subject by teacher
@login_required
def view_list(request):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        # if student has not updated his profile go back to profile and ask to update it
        if student_profile.section is None:
            messages.add_message(request, messages.ERROR,
                                 message="Update your profile before looking at other details")
            return redirect('profile')
        # get the subjects taught to the students and show it
        subjects = Teach.objects.filter(Class=student_profile.section)
        return render(request, 'marks/subject-list.html', {'subjects': subjects})
    elif is_teacher(request):
        # show the list of classes the teacher teaches
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'marks/subject-list.html', {'teaches': teaches})


# display student list for teacher
@login_required
def students_list(request, subjectId, classId):
    if is_teacher(request):
        # get list of students who are studying in the selected class
        class_obj = get_object_or_404(Class, id=classId)
        students_this_section = StudentProfile.objects.filter(section=class_obj)
        return render(request, 'marks/student-list.html', {'students': students_this_section, 'subjectId': subjectId})


# get details of marks of that particular student for teacher
@login_required
def student_marks_detail(request, classId, subjectId, studentId):
    if is_teacher(request):
        # get all the submissions made by the student
        student_profile = get_object_or_404(StudentProfile, id=studentId)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject__id=subjectId)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})


# get details of the the current logged in students marks of that subject
@login_required
def marks_detail(request, subjectId):
    if is_student(request):
        # get details of the student, for a selected subject
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        submissions = Submission.objects.filter(student=student_profile, assignment__subject__id=subjectId)
        return render(request, 'marks/subject-marks-detail.html', {'submissions': submissions})
