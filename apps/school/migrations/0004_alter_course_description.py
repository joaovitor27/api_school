# Generated by Django 3.2.20 on 2023-07-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
