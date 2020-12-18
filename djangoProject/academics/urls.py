from django.urls import path
import academics.views as academics_view

urlpatterns = [
    path('', academics_view.view_list, name="view-list"),
    path('<int:subjectId>', academics_view.view_notes, name="view-notes"),
]
