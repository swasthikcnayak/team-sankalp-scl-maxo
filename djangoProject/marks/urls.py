from django.urls import path
import marks.views as marks_view

urlpatterns = [
   path('', marks_view.view_list, name="view-list"),
   #path('/<int:subjectId>', marks_view.view_subject_marks, name="view-subject-marks"),
]
