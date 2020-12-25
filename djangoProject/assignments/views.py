from math import ceil

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import StudentProfile, TeacherProfile, Teach
from assignments.models import Submission, Assignment
from assignments.forms import AssignmentCreationForm, MarksUpdateForm, AssignmentSubmissionForm
from academics.models import Subject, Class


@login_required
def view_classes(request):
    if request.user.role == 'STD':
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        class_obj = student_profile.section
        subjects = Teach.objects.filter(Class=class_obj)
        return render(request, 'assignments/list-view.html', {'subjects': subjects,'classId':class_obj.id})
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
                          {'students': students_this_section, 'assignments': assignments_this_section_subject,
                           'form': form})
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
    elif request.user.role == 'STD':
        assignments = Assignment.objects.filter(subject__id=subjectId, Class__id=classId)
        return render(request,'assignments/assignment-detail.html',{'assignments':assignments})


@login_required
def submissions(request, assignmentId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        submission = Submission.objects.filter(assignment__id=assignmentId)
        if request.method == 'GET':
            form = MarksUpdateForm(assignment_id=assignmentId)
            return render(request, 'assignments/submission-list.html', {'submissions': submission, 'form': form})
        elif request.method == 'POST':
            form = MarksUpdateForm(request.POST)
            if form.is_valid():
                row = Submission.objects.get(id=assignmentId,
                                             student__user__username=form.cleaned_data['student'])
                row.marks_obtained = form.cleaned_data['marks_obtained']
                row.save()
                messages.success(request,
                                 message="Marks Updated Successfully")
                return render(request, 'assignments/submission-list.html', {'submissions': submission, 'form': form})
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details or contact admin")
            return render(request, 'assignments/submission-list.html', {'submissions': submission, 'form': form})
    elif request.user.role == 'STD':
        assignment_details = Assignment.objects.get(id=assignmentId)
        if request.method == 'GET':
            form = AssignmentSubmissionForm()
            return render(request, 'assignments/submission-list.html', {'assignment': assignment_details, 'form': form})
        elif request.method == 'POST':
            form = AssignmentSubmissionForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.assignment = Assignment.objects.get(id=assignmentId)
                student = StudentProfile.objects.get(user=request.user)
                answer.student = student
                answer.marks_obtained = -1
                answer.save()
                messages.success(request,
                                 message="Marks Updated Successfully")
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Could not submit assignment")
            form = AssignmentSubmissionForm(request.POST)
            return render(request, 'assignments/submission-list.html', {'assignment': assignment_details, 'form': form})


