from django.shortcuts import render

# Create your views here.
from .models import Student, Teacher, Subject, Class, School, Exam_Results,Timetable,Attendance

#Authentication Views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')  #get username from request
        password = request.data.get('password')   #get password from request
        user = authenticate(username=username, password=password)

        if user:        #if user exists
            refresh = RefreshToken.for_user(user) #generate token
            return Response({  #return token
                "refresh": str(refresh),   #refresh token
                "access": str(refresh.access_token),  #access token
            })
        return Response({"error": "Invalid credentials"}, status=400)  #return error message


#Student Views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import StudentSerializer

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]



#Teacher Views
from .serializers import TeacherSerializer

class TeacherListCreateView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]

class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


#Timetable Views
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import TimetableSerializer

class TimetableUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser) #allow file uploads
    permission_classes = [IsAdminUser] #only admin users can upload timetables

    def post(self, request):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)  #save the user who uploaded the timetable
            return Response(serializer.data, status=201)  #return the data/success
        return Response(serializer.errors, status=400)  #return error message

class TimetableListView(ListCreateAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

#Exam Results Views

from .serializers import Exam_ResultsSerializer

class Exam_ResultsUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = Exam_ResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class Exam_ResultsListView(ListCreateAPIView):
    queryset = Exam_Results.objects.all()
    serializer_class = Exam_ResultsSerializer

#class StudentResultView(APIView):
 #   def get(self, request, student_id):
  #      results = Exam_Result.objects.filter(student_id=student_id)
   #     serializer = Exam_ResultSerializer(results, many=True)
    #    return Response(serializer.data)
    
#Attendance Views

from .serializers import AttendanceSerializer

class MarkAttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AttendanceListView(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer