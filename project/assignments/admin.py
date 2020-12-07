from django.contrib import admin
from .models import Assignment, Submission


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'assignment_name', 'teacher', 'Class', 'start_time', 'end_time', 'maximum_marks')
    search_fields = ('subject', 'assignment_name', 'teacher', 'Class')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignments', 'student', 'time_submitted')
    search_fields = ('assignments', 'student')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
