from math import ceil

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import StudentProfile, TeacherProfile, Teach
from assignments.models import Submission, Assignment
from assignments.forms import AssignmentCreationForm
from academics.models import Subject, Class


@login_required
def view_classes(request):
    if request.user.role == 'STD':
        studentProfile = StudentProfile.objects.get(user=request.user)
        submissions = Submission.objects.filter(student=studentProfile)
        return render(request, 'assignments/list-view.html', {'submission': submissions})
    elif request.user.role == 'THR' or request.user.role == 'ADM':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        teaches = Teach.objects.filter(teacher=teacherProfile)
        return render(request, 'assignments/list-view.html', {'teaches': teaches})
    return redirect('/users/admin/attendance/attendance')


@login_required
def view_assignments(request, classId, subjectId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        form = AssignmentCreationForm()
        subject = Subject.objects.get(id=subjectId)
        class_obj = Class.objects.get(id=classId)
        students_this_section = StudentProfile.objects.filter(section=class_obj)
        if request.method == 'GET':
            assignments_this_section_subject = Assignment.objects.filter(subject=subject, Class=class_obj)
            return render(request, 'assignments/assignment-detail.html',
                          {'students': students_this_section, 'assignments': assignments_this_section_subject,'form': form})
        elif request.method == 'POST':
            teacherProfile = TeacherProfile.objects.get(user=request.user)
            form = AssignmentCreationForm(request.POST)
            if form.is_valid():
                assmt = form.save(commit=False)
                assmt.teacher = teacherProfile
                assmt.subject = subject
                assmt.Class = class_obj
                form.save()
                messages.success(request,
                                 message="Assignment added successfully")
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details")
            assignments_this_section_subject = Assignment.objects.filter(subject=subject, Class=class_obj)
            return render(request, 'assignments/assignment-detail.html', {'students': students_this_section,
                                                                          'assignments': assignments_this_section_subject,
                                                                          'form': form})


@login_required
def submissions(request, assignmentId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        submission = Submission.objects.filter(id=assignmentId)
        if request.method == 'GET':
            return render(request, 'assignments/submission-list.html', {'submissions': submission})
