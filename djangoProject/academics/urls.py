from django.urls import path
import academics.views as academics_view

urlpatterns = [
    path('notes/', academics_view.view_list, name="view-notes-subject-list"),  # list available subjects
    path('notes/<int:subjectId>', academics_view.view_notes, name="view-notes"),  # list the notes of selected subject
    path('class/', academics_view.class_list, name="view-class-list"),  # list available classes
    path('class/<int:classId>', academics_view.view_class, name="view-class"),  # view details of selected class
]
