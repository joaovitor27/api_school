from rest_framework import serializers
from .models import Student, Course, Registration
from .validators import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if not is_valid_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'CPF inválido. (Ex: 000.000.000-00)'}
            )
        if not is_valid_email(data['email']):
            raise serializers.ValidationError(
                {'email': 'Email inválido (Ex: joao@gmail.com)'}
            )
        if not is_valid_phone(data['phone']):
            raise serializers.ValidationError(
                {'phone': 'Telefone inválido (Ex: +5511900000000, +551100000000)'}
            )
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
