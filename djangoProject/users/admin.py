from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile, TeacherProfile, Teach


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

class TeachesAdminClass(admin.ModelAdmin):
    list_display = ('Class', 'subject', 'teacher')
    search_fields = ('Class__semester','Class__section_name','Class__department__department_name',
                        'Class__department__department_short_form','teacher__user__username', 
                        'teacher__user__email', 'teacher__user__first_name', 'teacher__user__lastname')


admin.site.register(User, UserAdminClass)
admin.site.register(StudentProfile, StudentProfileAdminClass)
admin.site.register(TeacherProfile, TeacherProfileAdminClass)
admin.site.register(Teach,TeachesAdminClass)