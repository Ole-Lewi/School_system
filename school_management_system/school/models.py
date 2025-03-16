from django.db import models

# Create your models here.
class  User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def _str_(self):
        return(self.username)
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.IntegerField(unique=True)
    assigned_class = models.CharField()

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