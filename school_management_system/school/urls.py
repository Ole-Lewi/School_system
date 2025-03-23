from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import LoginView, StudentListCreateView, StudentDetailView, TeacherListCreateView, TeacherDetailView, TimetableUploadView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('api/teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('api/timetable/', TimetableUploadView.as_view(), name='timetable-upload'),

]
