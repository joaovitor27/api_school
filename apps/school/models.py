import random
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Student(models.Model):
    name = models.CharField(verbose_name=_('Nome'), max_length=100)
    cpf = models.CharField(verbose_name=_('CPF'), max_length=14, unique=True)
    birth_date = models.DateField(verbose_name=_('Data de nascimento'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    phone = models.CharField(verbose_name=_('Telefone'), max_length=14, unique=True)
    active = models.BooleanField(verbose_name=_('Ativo'), default=True)

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')

    def __str__(self):
        """
        The __str__ function is a special function that returns the string representation of an object.
        The __str__ method is called when you print an object, or convert it to a string using str().
        If you don't define your own __str__ method, Python will use the default one.

        :param self: Refer to the class instance itself
        :return: The name of the object
        :doc-author: Trelent
        """
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', _('Básico')),
        ('I', _('Intermediário')),
        ('A', _('Avançado')),
    )

    code = models.CharField(verbose_name=_('Código'), max_length=8, unique=True)
    name = models.CharField(verbose_name=_('Nome'), max_length=100)
    description = models.TextField(verbose_name=_('Descrição'))
    level = models.CharField(verbose_name=_('Nível'), max_length=1, choices=LEVEL, blank=False, null=False, default='B')
    price = models.DecimalField(verbose_name=_('Preço'), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        """
        The __str__ function is called when you call str() on an object.
        It should return a string representation of the object.
        In this case, since we're working with a blog post, returning the title of the post seems like a good idea.

        :param self: Refer to the object itself
        :return: The name of the object
        :doc-author: Trelent
        """
        return self.name


class Registration(models.Model):
    PERIOD = (
        ('M', _('Matutino')),
        ('V', _('Vespertino')),
        ('N', _('Noturno')),
    )
    registration = models.CharField(verbose_name=_('Matrícula'), max_length=16, unique=True)
    student = models.ForeignKey(Student, verbose_name=_('Aluno'), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_('Curso'), on_delete=models.CASCADE)
    period = models.CharField(verbose_name=_('Período'), max_length=1, choices=PERIOD, blank=False, null=False,
                              default='M')

    class Meta:
        verbose_name = _('Matrícula')
        verbose_name_plural = _('Matrículas')

    def __str__(self):
        """
        The __str__ function is called when you call str() on an object.
        It should return a string representation of the object.
        In this case, since we're working with a blog post, returning the title of the post seems like a good idea.

        :param self: Refer to the object itself
        :return: The name of the object
        :doc-author: Trelent
        """
        return self.registration

    def set_registration(self) -> 'Registration':
        """
        The set_registration function is responsible for generating a registration number for the student.
        The registration number will be generated based on the current date and time, as well as the birth date of
        the student. The function returns an object of type Registration.

        :param self: Represent the instance of the class
        :return: The object itself
        :doc-author: Trelent
        """
        current_year: str = datetime.now().strftime('%Y')
        current_month: str = datetime.now().strftime('%m')
        current_day: str = datetime.now().strftime('%d')
        data_month: str = self.student.birth_date.strftime('%m')
        data_day: str = self.student.birth_date.strftime('%d')
        numbers_random: int = random.randint(1000, 9999)
        self.registration = f'{current_year}{current_month}{current_day}{data_day}{data_month}{str(numbers_random)}'
        return self
