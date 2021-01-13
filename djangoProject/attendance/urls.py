from django.urls import path
import attendance.views as attendance_view

urlpatterns = [
    path('', attendance_view.view_attendance, name="view-attendance"),
    # view attendance for student, get list of classes for teacher
    path('<int:classId>/<int:subjectId>', attendance_view.view_subject_attendance, name="view-subject-attendance"),
    # view and update attendance for teacher student not allowed
]
