#serializers converts data into JSON format so that it can be easily rendered into a template.
#In the below I have created serializers for the Student, Teacher, Exam_Results, Timetable, and Attendance models.

from .models import Student, Teacher, Exam_Results,Timetable,Attendance
from rest_framework import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class TeacherSerializer(ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

class Exam_ResultsSerializer(ModelSerializer):
    class Meta:
        model=Exam_Results
        fields='__all__'

class TimetableSerializer(ModelSerializer):
    class Meta:
        model=Timetable
        fields='__all__'

class AttendanceSerializer(ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
