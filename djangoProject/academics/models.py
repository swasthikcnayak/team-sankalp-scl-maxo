from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=50, null=True, unique=True)
    department_short_form = models.CharField(max_length=4, null=True, unique=True)

    def __str__(self):
        return self.department_short_form

    def clean(self):
        self.department_short_form = self.department_short_form.upper()
        self.department_name = self.department_name.upper()


class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    subject_name = models.CharField(max_length=50, null=True)
    subject_short_form = models.CharField(max_length=4, null=True)
    credits = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.department.department_short_form + "+" + self.subject_short_form

    class Meta:
        unique_together = ('department', 'subject_short_form')

    def clean(self):
        self.subject_short_form = self.subject_short_form.upper()
        self.subject_name = self.subject_name.upper()


SEM_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)

SECTION_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


class Class(models.Model):
    semester = models.CharField(max_length=3, choices=SEM_CHOICES, default='1')
    section_name = models.CharField(max_length=1, choices=SECTION_CHOICES, default='A')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    timetable = models.FileField(upload_to='timetable')

    def clean(self):
        self.section_name = self.section_name.upper()

    class Meta:
        unique_together = ('semester', 'section_name', 'department')

    def __str__(self):
        return self.department.department_short_form + "+" + self.semester + "+" + self.section_name


class Note(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='department', null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="subject")
    chapter_number = models.CharField(max_length=2, null=True)
    chapter_name = models.CharField(max_length=50, null=True)
    link = models.FileField(upload_to='notes')

    class Meta:
        unique_together = ('department', 'subject', 'chapter_number')

    def __str__(self):
        return self.department.department_short_form + "+" + self.subject.subject_short_form + "+" + self.chapter_number
