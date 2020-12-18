from django.db import models

from academics.models import Subject, Class
from users.models import StudentProfile, TeacherProfile


class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name="student")
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name="teacher", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="subject")
    Class = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)
    classes_conducted = models.IntegerField()
    classes_attended = models.IntegerField()
    percentage = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject')


class AttendanceLog(models.Model):
    absentees = models.ManyToManyField(StudentProfile, verbose_name='absentees', blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='subject',null=False)
    Class = models.ForeignKey(Class,on_delete=models.CASCADE,verbose_name='class',null=False)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name='teacher', null=True)
    conducted_date = models.DateField( null=True,verbose_name='conducted_date')
    logged_date = models.DateTimeField(auto_now_add=True, verbose_name='logged_date')

    class Meta:
        unique_together = ('conducted_date', 'subject','Class')