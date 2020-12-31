from math import ceil

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from djangoProject.utils import is_student, is_teacher
from users.models import StudentProfile, TeacherProfile, Teach
from assignments.models import Submission, Assignment
from assignments.forms import AssignmentCreationForm, MarksUpdateForm, AssignmentSubmissionForm
from academics.models import Subject, Class


@login_required
def view_classes(request):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        if student_profile.section is None:
            messages.add_message(request, messages.ERROR,
                                 message="Update your profile before looking at other details")
            return redirect('profile')
        subjects = Teach.objects.filter(Class=student_profile.section)
        return render(request, 'assignments/list-view.html',
                      {'subjects': subjects, 'classId': student_profile.section.id})
    elif is_teacher(request):
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'assignments/list-view.html', {'teaches': teaches})


@login_required
def view_assignments(request, classId, subjectId):
    if is_teacher(request):
        form = AssignmentCreationForm()
        subject = get_object_or_404(Subject, id=subjectId)
        class_obj = get_object_or_404(Class, id=classId)
        if request.method == 'GET':
            assignments_this_section_subject = Assignment.objects.filter(subject=subject, Class=class_obj)
            return render(request, 'assignments/assignment-detail.html',
                          {'assignments': assignments_this_section_subject,
                           'form': form})
        elif request.method == 'POST':
            teacherProfile = TeacherProfile.objects.get(user=request.user)
            form = AssignmentCreationForm(request.POST,request.FILES)
            if form.is_valid():
                assmt = form.save(commit=False)
                assmt.teacher = teacherProfile
                assmt.subject = subject
                assmt.Class = class_obj
                form.save()
                messages.success(request,
                                 message="Assignment added successfully")
            else:
                print(form.errors)
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details")
            return redirect('view-subject-assignment', subjectId=subjectId, classId=classId)
    elif is_student(request):
        assignments = Assignment.objects.filter(subject__id=subjectId, Class__id=classId)
        return render(request, 'assignments/assignment-detail.html', {'assignments': assignments})


@login_required
def submissions(request, assignmentId):
    assignment_details = get_object_or_404(Assignment, id=assignmentId)
    if is_teacher(request):
        submission = Submission.objects.filter(assignment__id=assignmentId)
        if request.method == 'GET':
            form = MarksUpdateForm()
            form.fields['student'].queryset = StudentProfile.objects.filter(submission__assignment__id = assignmentId)
            return render(request, 'assignments/submission-list.html', {'submissions': submission, 'form': form,
                                                                        'assignment':assignment_details})
        elif request.method == 'POST':
            form = MarksUpdateForm(request.POST)
            if form.is_valid():
                row = Submission.objects.get(assignment__id=assignmentId,
                                             student__user__username=form.cleaned_data['student'])
                print(row.answer)
                row.marks_obtained = form.cleaned_data['marks_obtained']
                row.save()
                messages.success(request,
                                 message="Marks Updated Successfully")
            else:
                print(form.errors)
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details or contact admin")
            return redirect('view-submissions',assignmentId=assignmentId)
    elif is_student(request):
        if request.method == 'GET':
            form = AssignmentSubmissionForm()
            return render(request, 'assignments/submission-list.html', {'assignment': assignment_details, 'form': form})
        elif request.method == 'POST':
            form = AssignmentSubmissionForm(request.POST,request.FILES)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.assignment = Assignment.objects.get(id=assignmentId)
                student = StudentProfile.objects.get(user=request.user)
                answer.student = student
                answer.marks_obtained = -1
                answer.save()
                messages.success(request,
                                 message="Assignment submitted Successfully")
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Could not submit assignment")
            return redirect('view-submissions',assignmentId=assignmentId)
