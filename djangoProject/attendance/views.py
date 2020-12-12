"""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from attendance.models import Attendance
from users.models import StudentProfile, TeacherProfile, Teach
from academics.models import Subject


@login_required
def view_attendance(request):
    if request.user.role == 'STD':
        studentProfile = StudentProfile.objects.get(user=request.user)
        subjects = Attendance.objects.filter(studentProfile=studentProfile).values('subject').distinct()
        print(subjects)
        render('attendance.html', {'subjects': subjects})
    elif request.user.role == 'THR':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        teaches = Teach.objects.filter(teacher=teacherProfile)
        print(teaches)
        render('attendance.html', {'classes': teaches})


@login_required
def view_subject_attendance(request, subjectId):
    if request.user.role == 'STD':
        studentProfile = StudentProfile.objects.get(user=request.user)
        subject = Subject.objects.get(id=subjectId)
        attendances = Attendance.objects.filter(student=studentProfile, subject=subject)
        print(attendances)
        render('attendance.html', {'attendances': attendances})
    elif request.user.role == 'THR':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        subject = Subject.objects.get(id=subjectId)
        render('attendance.html',{'subject':subject}) """

# we can get the class of the user logged in from his profile. using the teaches model
# we can then find all the subjects taught to that class, which can form a drop down list.


# we can access Teach model using the teacher profile. which gives us the class and the subject that he teacher
# using which, we can get list of all students belonging to that class.
