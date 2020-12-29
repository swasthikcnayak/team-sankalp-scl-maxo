from django.urls import path
import marks.views as marks_view

urlpatterns = [
    path('', marks_view.view_list, name="view-list"),  # get list of subjects
    path('<int:subjectId>/', marks_view.marks_detail, name="view_marks_detail"),  # get details by student about himself
    path('<int:subjectId>/<int:classId>', marks_view.students_list, name="view_marks_list_student"),
    # get list of students
    path('<int:subjectId>/<int:classId>/<int:studentId>', marks_view.student_marks_detail,
         name="view_marks_detail_student"),  # get details of the student query by teacher
]
