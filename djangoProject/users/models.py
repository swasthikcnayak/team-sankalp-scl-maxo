from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image

from academics.models import Department

from academics.models import Subject, Class, SEM_CHOICES


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email Id")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email),
                          username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.role = 'ADM'
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", unique=True)
    ROLE_CHOICES = [
        ('STD', 'STUDENT'),
        ('THR', 'TEACHER'),
        ('ADM', 'ADMIN')
    ]
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='STD')
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    blood_group = models.CharField(max_length=4, null=True)
    address_line_1 = models.CharField(max_length=50, null=True)
    address_line_2 = models.CharField(max_length=50, null=True)
   #address_line_3 = models.CharField(max_length=50, null=True)

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    class Meta:
        unique_together = ('role', 'username')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name="department", null=True,
                                   default=None)
    semester = models.CharField(max_length=3, choices=SEM_CHOICES, default='1')
    section = models.ForeignKey(Class, on_delete=models.SET_NULL, verbose_name="section", null=True, default=None)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def clean(self):
        self.cgpa = abs(self.cgpa)

    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name="department", null=True)
    join_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class Teach(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="section")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('Class', 'subject', 'teacher')
