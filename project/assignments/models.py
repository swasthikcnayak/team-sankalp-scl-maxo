from django.db import models

# from academics.models import Subject, Class
from users.models import StudentProfile, TeacherProfile


class Assignment(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name="teacher", null=True)
    # Class = models.ForeignKey(Class, on_delete=models.SET_NULL, verbose_name='class', null=True)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='subject')
    assignment_name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    maximum_marks = models.CharField(max_length=3)
    question = models.URLField()

    def clean(self):
        self.assignment_name = self.assignment_name.upper()

    '''def __str__(self):
        return self.assignment_name + "+" + self.Class + "+" + self.subject'''

    class Meta:
        unique_together = ('subject', 'assignment_name')


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name='assignments')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name='student')
    answer = models.URLField()
    time_submitted = models.DateTimeField()

    '''def __str__(self):
        return self.assignments + "+" + self.student'''

    class Meta:
        unique_together = ('assignments', 'student')
