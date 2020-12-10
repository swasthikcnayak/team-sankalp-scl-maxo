from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile, TeacherProfile, Attendance, Mark


class UserAdminClass(UserAdmin):
    list_display = ('email', 'username', 'role', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StudentProfileAdminClass(admin.ModelAdmin):
    list_display = ('user', 'department', 'semester', 'section', 'cgpa')
    search_fields = ('user__username', 'user__email', 'department__department_short_form',
                     'department__department_name', 'user__first_name', 'user__last_name', 'section', 'cgpa')


class TeacherProfileAdminClass(admin.ModelAdmin):
    list_display = ('user', 'department', 'join_date')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__lastname',
                     'department__department_short_form', 'department__department_name')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'classes_attended', 'classes_conducted', 'percentage')
    search_fields = ('student__user__username', 'student__user__email', 'student__user__first_name',
                     'student__user__last_name', 'subject__department__department_short_form',
                     'subject__department__department_name','teacher__user__username','teacher__user__first_name')


class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'teacher', 'marks_obtained', 'marks_maximum')
    search_fields = ('student__user__username', 'student__user__email', 'student__user__first_name',
                     'student__user__last_name', 'subject__subject_name','subject__subject_short_form',
                     'subject__department__department_short_form', 'subject__department__department_name')


admin.site.register(User, UserAdminClass)
admin.site.register(StudentProfile, StudentProfileAdminClass)
admin.site.register(TeacherProfile, TeacherProfileAdminClass)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Mark, MarksAdmin)