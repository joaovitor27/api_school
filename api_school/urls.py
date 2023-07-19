from django.contrib import admin
from django.urls import path, include
from school.views import (StudentViewSet, CourseViewSet, RegistrationViewSet, ListRegistrationStudent,
                          ListRegistrationStudentCourse)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('course', CourseViewSet, basename='course')
router.register('registration', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registration/', ListRegistrationStudent.as_view()),
    path('course/<int:pk>/registration/', ListRegistrationStudentCourse.as_view()),
]
