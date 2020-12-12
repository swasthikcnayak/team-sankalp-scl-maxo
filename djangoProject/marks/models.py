from django.db import models

from academics.models import Subject
from users.models import StudentProfile, TeacherProfile


class Mark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name="student")
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name="teacher", null=True)
    exam_name = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="subject")
    marks_maximum = models.CharField(max_length=3)
    marks_obtained = models.CharField(max_length=3)

    def clean(self):
        self.exam_name = self.exam_name.upper()

    class Meta:
        unique_together = ('student', 'subject', 'exam_name')
