# Generated by Django 3.2.20 on 2023-07-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20230719_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=8, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='student',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=13, unique=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='student',
            name='rg',
            field=models.CharField(max_length=7, unique=True, verbose_name='RG'),
        ),
    ]
