from django.urls import path
import assignments.views  as  assmt_view

urlpatterns = [
    path('', assmt_view.view_classes, name="view-classes-assignment"),  # list of subjects / list of classes
    path('<int:classId>/<int:subjectId>', assmt_view.view_assignments, name="view-subject-assignment"),
    # list of assignments
    path('submissions/<int:assignmentId>', assmt_view.submissions, name="view-submissions"),  # submissions
]
