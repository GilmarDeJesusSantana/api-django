# Generated by Django 4.0.3 on 2022-03-15 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_matriculas_periodo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matriculas',
            new_name='Matricula',
        ),
    ]