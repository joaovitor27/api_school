from rest_framework import serializers
from .models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class ListRegistrationStudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Registration
        fields = ['id', 'registration', 'student', 'course', 'period']


class ListRegistrationCourseStudentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Registration
        fields = ['student']
