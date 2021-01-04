from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from academics.models import Subject, Class
from assignments.forms import AssignmentCreationForm, MarksUpdateForm, AssignmentSubmissionForm
from assignments.models import Submission, Assignment
from djangoProject.utils import is_student, is_teacher
from users.models import StudentProfile, TeacherProfile, Teach


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
    time_now = timezone.now()
    assignment_parred_due_date = Assignment.objects.filter(subject__id=subjectId, Class__id=classId,
                                                           start_time__lt=time_now, end_time__lt=time_now)
    assignments_to_complete = Assignment.objects.filter(subject__id=subjectId, Class__id=classId,
                                                        start_time__lt=time_now, end_time__gt=time_now)
    assignments_scheduled = Assignment.objects.filter(subject__id=subjectId, Class__id=classId,
                                                      start_time__gt=time_now, end_time__gt=time_now)
    if is_teacher(request):
        form = None
        subject = get_object_or_404(Subject, id=subjectId)
        class_obj = get_object_or_404(Class, id=classId)
        if request.method == 'GET':
            form = AssignmentCreationForm()
        elif request.method == 'POST':
            teacherProfile = TeacherProfile.objects.get(user=request.user)
            form = AssignmentCreationForm(request.POST, request.FILES)
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
        return render(request, 'assignments/assignment-detail.html',
                      {'assignment_parred_due_date': assignment_parred_due_date,
                       'assignments_to_complete': assignments_to_complete,
                       'assignments_scheduled': assignments_scheduled,
                       'form': form})
    elif is_student(request):
        return render(request, 'assignments/assignment-detail.html',
                      {'assignment_parred_due_date': assignment_parred_due_date,
                       'assignments_to_complete': assignments_to_complete,
                       'assignments_scheduled': assignments_scheduled})


@login_required
def submissions(request, assignmentId):
    form = None
    assignment_details = get_object_or_404(Assignment, id=assignmentId)
    if is_teacher(request):
        submission = Submission.objects.filter(assignment__id=assignmentId)
        if request.method == 'GET':
            form = MarksUpdateForm()
            form.fields['student'].queryset = StudentProfile.objects.filter(submission__assignment__id=assignmentId)
        elif request.method == 'POST':
            form = MarksUpdateForm(request.POST)
            if form.is_valid():
                row = Submission.objects.get(assignment__id=assignmentId,
                                             student__user__username=form.cleaned_data['student'])
                row.marks_obtained = form.cleaned_data['marks_obtained']
                row.save()
                messages.success(request,
                                 message="Marks Updated Successfully")
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details or contact admin")
        return render(request, 'assignments/submission-list.html', {'submissions': submission, 'form': form,
                                                                    'assignment': assignment_details})
    elif is_student(request):
        submission = Submission.objects.filter(assignment=assignment_details, student__user=request.user).first()
        if request.method == 'GET':
            if submission is None:
                submission = 0
            form = AssignmentSubmissionForm()
        elif request.method == 'POST':
            time_now = timezone.now()
            if time_now > assignment_details.end_time or time_now < assignment_details.start_time:
                messages.add_message(request, messages.ERROR,
                                     message="You missed your assignment deadline, contact your teacher")
                return redirect('view-classes-assignment')
            form = AssignmentSubmissionForm(request.POST, request.FILES)
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
        return render(request, 'assignments/submission-list.html',
                      {'assignment': assignment_details, 'form': form, 'submission': submission})
