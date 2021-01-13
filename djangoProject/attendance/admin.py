from django.contrib import admin

from attendance.models import Attendance
from attendance.models import AttendanceLog


# show details of attendance in admin panel
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'classes_attended', 'classes_conducted', 'percentage')
    search_fields = ('student__user__username', 'student__user__email', 'student__user__first_name',
                     'student__user__last_name', 'subject__department__department_short_form',
                     'subject__department__department_name')


# logging of attendance in admin panel
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('Class', 'teacher', 'subject', 'conducted_date', 'logged_date')
    search_fields = ('absentees__user__username', 'absentees__user__email', 'absentees__user__first_name',
                     'absentees__user__last_name', 'Class__semester', 'Class__section_name',
                     'subject__subject_short_from', 'subject__subject_name',
                     'subject__department__department_short_form',
                     'subject__department__department_name', 'teacher__user__username', 'teacher__user__first_name')


# registing the new Models with the admin site
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceLog, AttendanceLogAdmin)
