from rest_framework import serializers
from .models import Student, Course, Registration
from .validators import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if not is_valid_cpf(data['cpf']):
            raise serializers.ValidationError('CPF inválido')
        if not is_valid_rg(data['rg']):
            raise serializers.ValidationError('RG inválido')
        if not is_valid_name(data['name']):
            raise serializers.ValidationError('Nome não pode conter números')
        return data

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
