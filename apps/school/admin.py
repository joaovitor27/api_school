from django.contrib import admin
from .models import Student, Course, Registration


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'birth_date', 'email', 'phone', 'registration')
    list_display_links = ('id', 'name', 'cpf', 'email', 'phone', 'registration')
    search_fields = ('name', 'rg', 'cpf', 'email', 'registration')
    list_per_page = 15
    ordering = ('name',)


admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'description', 'level', 'price')
    list_display_links = ('id', 'code', 'name')
    search_fields = ('name', 'code', 'level', 'price')
    list_per_page = 15


admin.site.register(Course, CourseAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration', 'student', 'course')
    list_display_links = ('id', 'registration', 'student', 'course')
    search_fields = ('student', 'registration', 'course')
    list_per_page = 15


admin.site.register(Registration, RegistrationAdmin)
