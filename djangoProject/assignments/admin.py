from django.contrib import admin
from .models import Assignment, Submission


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'assignment_name', 'teacher', 'Class', 'start_time', 'end_time', 'maximum_marks')
    search_fields = ('assignment_name', 'teacher__user__username','subject__subject_name','subject__subject_short_form',
                     'teacher__user__first_name', 'Class__section_name', 'Class__department__department_short_form',
                     'Class__department__department_name')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'time_submitted')
    search_fields = ('assignment__assignment_name', 'assignment__subject__subject_name','student__user__username',
                     'student__user__first_name','assignment__Class__section_name',
                     'assignment__Class__department__department_name',
                     'assignment__Class__department__department_short_form',
                     'assignment__subject__subject_short_form',
                     )


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
