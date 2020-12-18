from math import ceil

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.models import Attendance
from users.models import StudentProfile, TeacherProfile, Teach
from academics.models import Subject, Class
from attendance.forms import AttendanceUpdateForm
from django.contrib import messages


@login_required
def view_attendance(request):
    if request.user.role == 'STD':
        studentProfile = StudentProfile.objects.get(user=request.user)
        attendances = Attendance.objects.filter(student=studentProfile)
        return render(request, 'attendance/attendance.html', {'attendances': attendances})
    elif request.user.role == 'THR' or request.user.role == 'ADM':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        teaches = Teach.objects.filter(teacher=teacherProfile)
        return render(request, 'attendance/attendance.html', {'teaches': teaches})
    return redirect('/users/admin/attendance/attendance')


@login_required
def view_subject_attendance(request, classId, subjectId):
    if request.user.role == 'THR' or request.user.role == 'ADM':
        subject = Subject.objects.get(id=subjectId)
        class_obj = Class.objects.get(id=classId)
        form = AttendanceUpdateForm()
        attendances = Attendance.objects.filter(subject=subject, student__section=class_obj)
        if request.method == 'GET':
            return render(request, 'attendance/attendance-edit.html', {'attendances': attendances, 'form': form})
        elif request.method == 'POST':
            teacherProfile = TeacherProfile.objects.get(user=request.user)
            form = AttendanceUpdateForm(request.POST)
            if form.is_valid():
                log = form.save(commit=False)
                log.teacher = teacherProfile
                log.subject = subject
                log.Class = class_obj
                log = form.save()
                attendances = Attendance.objects.filter(Class=class_obj, subject=subject)

                for attendance in attendances:
                    attendance.classes_conducted = attendance.classes_conducted + 1
                    if attendance.student not in log.absentees.all():
                        attendance.classes_attended = attendance.classes_attended + 1
                    attendance.percentage = ceil(attendance.classes_attended / attendance.classes_conducted * 100)
                    attendance.save()
                    messages.success(request,
                                 message="Absentees registered successfully")
                return render(request, 'attendance/attendance-edit.html', {'attendances': attendances, 'form': form})
