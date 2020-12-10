from django.db import models

from academics.models import Subject
from users.models import StudentProfile, TeacherProfile


class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name="student")
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name="teacher", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="subject")
    classes_conducted = models.CharField(max_length=3)
    classes_attended = models.CharField(max_length=3)
    percentage = models.CharField(max_length=4)

    class Meta:
        unique_together = ('student', 'subject')
