from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Student, Course, Registration
from .serializer import (StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializer,
                         ListRegistrationCourseStudentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', ]
    search_fields = ['name', 'cpf', 'email']
    filterset_fields = ['active', ]
    http_method_names = ['get', 'post', 'put', 'patch']


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id_course = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response['Location'] = request.build_absolute_uri() + id_course
            return response


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @method_decorator(cache_page(20))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(request, *args, **kwargs)


class ListRegistrationStudent(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ListRegistrationStudentSerializer
    http_method_names = ['get']

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
    http_method_names = ['get']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
