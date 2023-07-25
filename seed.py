import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_school.settings')
django.setup()

from school.models import Course


def criando_cursos(quantidade_de_cursos):
    Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        descs = ['Python Fundamentos', 'Python intermediário', 'Python Avançado', 'Python para Data Science',
                 'Python/React']
        description = random.choice(descs)
        cod_curso = "{}{}-{}".format(description[:3].upper(), random.randrange(100, 999), random.randrange(1, 9))
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(code=cod_curso, name=description, description=description, level=level,
                   price=random.randrange(100, 999))
        c.save()


criando_cursos(5)
