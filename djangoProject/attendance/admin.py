from django.contrib import admin

from attendance.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'classes_attended', 'classes_conducted', 'percentage')
    search_fields = ('student__user__username', 'student__user__email', 'student__user__first_name',
                     'student__user__last_name', 'subject__department__department_short_form',
                     'subject__department__department_name','teacher__user__username','teacher__user__first_name')


admin.site.register(Attendance, AttendanceAdmin)