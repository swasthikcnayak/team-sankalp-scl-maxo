"""from django.contrib import admin

from marks.models import Mark


class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'teacher', 'marks_obtained', 'marks_maximum')
    search_fields = ('student__user__username', 'student__user__email', 'student__user__first_name',
                     'student__user__last_name', 'subject__subject_name','subject__subject_short_form',
                     'subject__department__department_short_form', 'subject__department__department_name')


admin.site.register(Mark, MarksAdmin)"""