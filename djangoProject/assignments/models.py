from django.db import models
from academics.models import Subject, Class
from users.models import StudentProfile, TeacherProfile


class Assignment(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, verbose_name="teacher", null=True)
    Class = models.ForeignKey(Class, on_delete=models.SET_NULL, verbose_name='class', null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='subject')
    assignment_name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    maximum_marks = models.CharField(max_length=3)
    question = models.FileField(upload_to='assignments')
    description = models.TextField(null=True)

    def clean(self):
        self.assignment_name = self.assignment_name.upper()

    def __str__(self):
        return str(self.Class.semester) + "+" + str(self.Class.section_name) + "+" + str(
            self.subject) + "+" + self.assignment_name

    class Meta:
        unique_together = ('subject', 'assignment_name', 'Class')


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name='assignment')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name='student')
    answer = models.FileField(upload_to='submissions')
    time_submitted = models.DateTimeField(auto_now_add=True)
    marks_obtained = models.IntegerField(null=True)

    def __str__(self):
        return str(self.assignment.subject.subject_short_form) + "+" + str(self.assignment.assignment_name) + "+" + str(
            self.student)

    class Meta:
        unique_together = ('assignment', 'student')
