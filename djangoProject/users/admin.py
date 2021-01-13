from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile, TeacherProfile, Teach


# changing admin view for user profile
# list_display refers to the list of columns that admin should be able to see
class UserAdminClass(UserAdmin):
    # list to display in admin panel
    list_display = ('username', 'email', 'role', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    # search by following fields
    search_fields = ('email', 'username')
    # cannot be edited
    readonly_fields = ('date_joined', 'last_login')

    # required features that should be overriding the UserAdmin,
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# changing admin view for student profile
class StudentProfileAdminClass(admin.ModelAdmin):
    list_display = ('user', 'department', 'semester', 'section', 'cgpa')
    search_fields = ('user__username', 'user__email', 'department__department_short_form',
                     'department__department_name', 'user__first_name', 'user__last_name', 'section', 'cgpa')


# changing admin view for teacher profile
class TeacherProfileAdminClass(admin.ModelAdmin):
    list_display = ('user', 'department', 'join_date')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__lastname',
                     'department__department_short_form', 'department__department_name')


# changing admin view for teahes model
class TeachesAdminClass(admin.ModelAdmin):
    list_display = ('teacher', 'Class', 'subject')
    search_fields = ('Class__semester', 'Class__section_name', 'Class__department__department_name',
                     'Class__department__department_short_form', 'teacher__user__username',
                     'teacher__user__email', 'teacher__user__first_name', 'teacher__user__lastname')


# registering the models and the corresponding admiv view for admin
admin.site.register(User, UserAdminClass)
admin.site.register(StudentProfile, StudentProfileAdminClass)
admin.site.register(TeacherProfile, TeacherProfileAdminClass)
admin.site.register(Teach, TeachesAdminClass)
