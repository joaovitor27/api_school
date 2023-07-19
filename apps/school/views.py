from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Student, Course, Registration
from .serializer import (StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer,
                         ListRegistrationCourseStudentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListRegistrationStudent(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ListRegistrationStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset


class ListRegistrationStudentCourse(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ListRegistrationCourseStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
