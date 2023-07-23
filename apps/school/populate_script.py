import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_school.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from school import models


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate(mask=True)
        celular = "+55{}9{}{}".format(random.randrange(10, 21),
                                      random.randrange(4000, 9999),
                                      random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        p = models.Student(name=nome, email=email, cpf=cpf, phone=celular, active=ativo)
        p.save()


criando_pessoas(150)
