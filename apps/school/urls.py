from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'school'

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')
router.register('course', views.CourseViewSet, basename='course')
router.register('registration', views.RegistrationViewSet, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:pk>/registration/', views.ListRegistrationStudent.as_view()),
    path('course/<int:pk>/registration/', views.ListRegistrationStudentCourse.as_view()),
]
