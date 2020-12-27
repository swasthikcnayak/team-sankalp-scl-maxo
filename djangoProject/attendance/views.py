from math import ceil
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from attendance.models import Attendance, AttendanceLog
from djangoProject.utils import is_student, is_teacher
from users.models import StudentProfile, TeacherProfile, Teach
from academics.models import Subject, Class
from attendance.forms import AttendanceUpdateForm, RequestAttendanceDetails
from django.contrib import messages


# teacher will be able to get list of classes he teaches and student will be able to see his attendances in various
# subjects
@login_required
def view_attendance(request):
    if is_student(request):
        studentProfile = get_object_or_404(StudentProfile, user=request.user)
        if request.method == 'GET':
            form = RequestAttendanceDetails(semester=studentProfile.semester)
            attendances = Attendance.objects.filter(student=studentProfile, Class__id=studentProfile.section.id)
            return render(request, 'attendance/attendance.html', {'attendances': attendances, 'form': form})
        elif request.method == 'POST':
            form = RequestAttendanceDetails(request.POST)
            selected_sem = ""
            if form.is_valid():
                selected_sem = form.cleaned_data['semester']
                attendances = Attendance.objects.filter(student=studentProfile, Class__semester=selected_sem)
                if attendances.count() != 0:
                    messages.success(request,
                                     message="Showing details of selected semester attendance")
                else:
                    messages.add_message(request, messages.ERROR,
                                         message="No record found in this semester")
            attendances = Attendance.objects.filter(student=studentProfile, Class__semester=selected_sem)
            return render(request, 'attendance/attendance.html', {'attendances': attendances, 'form': form})
    elif is_teacher(request):
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'attendance/attendance.html', {'teaches': teaches})


@login_required
def view_subject_attendance(request, classId, subjectId):
    if is_teacher(request):
        subject = get_object_or_404(Subject, id=subjectId)
        class_obj = get_object_or_404(Class, id=classId)
        form = AttendanceUpdateForm(class_obj=class_obj)
        students_this_section = StudentProfile.objects.filter(section=class_obj)
        for students in students_this_section:
            if not Attendance.objects.filter(student=students, subject=subject, Class=class_obj).exists():
                Attendance.objects.create(student=students, subject=subject, Class=class_obj)
        attendances = Attendance.objects.filter(subject=subject, Class=class_obj)
        try:
            last_updated = AttendanceLog.objects.filter(subject=subject, Class=class_obj).order_by('-logged_date'). \
                first().logged_date
        except AttendanceLog.DoesNotExist:
            last_updated = None
        if request.method == 'GET':
            return render(request, 'attendance/attendance-edit.html', {'attendances': attendances, 'form': form,
                                                                       'date_last_updated': last_updated})
        elif request.method == 'POST':
            teacherProfile = get_object_or_404(TeacherProfile, user=request.user)
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
            else:
                messages.add_message(request, messages.ERROR,
                                     message="Please check the input details")
            return redirect('view-subject-attendance', classId=classId, subjectId=subjectId)
