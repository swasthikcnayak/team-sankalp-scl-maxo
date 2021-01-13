from django.db import models


# Model for department with suitable entries
class Department(models.Model):
    department_name = models.CharField(max_length=50, null=True, unique=True)
    department_short_form = models.CharField(max_length=4, null=True, unique=True)

    # show the shortform for the department wherever used
    def __str__(self):
        return self.department_short_form

    # convert to uppercase for uniformity
    def clean(self):
        self.department_short_form = self.department_short_form.upper()
        self.department_name = self.department_name.upper()


# Model for every subject
class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    subject_name = models.CharField(max_length=50, null=True)
    subject_short_form = models.CharField(max_length=4, null=True)
    credits = models.CharField(max_length=1, null=True)

    # show the department along with subject wherever used
    def __str__(self):
        return self.department.department_short_form + "+" + self.subject_short_form

    # department and subject must be unique together
    class Meta:
        unique_together = ('department', 'subject_short_form')

    # converting the inputs to upper case for uniformity
    def clean(self):
        self.subject_short_form = self.subject_short_form.upper()
        self.subject_name = self.subject_name.upper()


# avaiable semester choices
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

# avaiable section choices
SECTION_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


# Class model involving details of the class
class Class(models.Model):
    semester = models.CharField(max_length=3, choices=SEM_CHOICES, default='1')
    section_name = models.CharField(max_length=1, choices=SECTION_CHOICES, default='A')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    timetable = models.FileField(upload_to='timetable')

    # section name transformed to uppercase
    def clean(self):
        self.section_name = self.section_name.upper()

    # only one entry for a semester,department and section name
    class Meta:
        unique_together = ('semester', 'section_name', 'department')

    # display the class
    def __str__(self):
        return self.department.department_short_form + "+" + self.semester + "+" + self.section_name


# Notes model for storing notes
class Note(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='department', null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="subject")
    chapter_number = models.CharField(max_length=2, null=True)
    chapter_name = models.CharField(max_length=50, null=True)
    link = models.FileField(upload_to='notes')

    class Meta:
        # only one notes for a chapter number,subject and department
        unique_together = ('department', 'subject', 'chapter_number')

    def __str__(self):
        return self.department.department_short_form + "+" + self.subject.subject_short_form + "+" + self.chapter_number
