from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, role, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, role="admin", password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for Django admin

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Required for authentication
    REQUIRED_FIELDS = ['full_name','email']  # Required when user is created

    def __str__(self):
        return f"{self.full_name} ({self.role})"

    
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    admission_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    class_assigned = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=50)
    parent_phone_number = models.IntegerField()
    parent_email = models.EmailField()

    def _str_(self):
        return(self.user.username)
    
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_id = models.IntegerField(unique=True)
    assigned_class = models.CharField(max_length=50)

    def _str_(self):
        return(self.user.username)
    
class Class(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def _str_(self):
        return(self.name)
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def _str_(self):
        return(self.student.user.username)
    
class Timetable(models.Model):
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.FileField(upload_to='timetables/')

    def _str_(self):
        return(self.timetable.name)
    
class Exam_Results(models.Model):
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date_uploaded = models.DateField()
    exam_name = models.CharField(max_length=50)
    file = models.FileField(upload_to= 'exam_results/')

    def _str_(self):
        return(self.exam.name)