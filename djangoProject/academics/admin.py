from django.contrib import admin
from .models import Department, Subject, Class, Note


class DepartmentAdminModel(admin.ModelAdmin):
    list_display = ('department_name', 'department_short_form')
    search_fields = ('department_name', 'department_short_form')


class SubjectAdminModel(admin.ModelAdmin):
    list_display = (
        'department',
        'subject_name', 'subject_short_form',
        'credits')
    search_fields = (
        'department__department_short_form',
        'department__department_name',
        'subject_name', 'subject_short_form',
        'credits')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ClassAdminModel(admin.ModelAdmin):
    list_display = (
        'department',
        'semester',
        'section_name',
    )
    search_fields = (
        'semester',
        'section_name', 'department__department_short_form',
        'department__department_name'
    )


class NotesAdminModel(admin.ModelAdmin):
    list_display = (
        'department',
        'subject',
        'chapter_number',
        'chapter_name',
    )
    search_fields = (
        'department__department_name',
        'department__department_short_form',
        'subject__subject_name',
        'subject__subject_short_form',
        'chapter_name',
        'chapter_number',
    )


admin.site.register(Department, DepartmentAdminModel)
admin.site.register(Subject, SubjectAdminModel)
admin.site.register(Class, ClassAdminModel)
admin.site.register(Note, NotesAdminModel)
