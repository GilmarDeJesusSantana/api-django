# Generated by Django 4.0.3 on 2022-03-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matriculas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculas',
            name='periodo',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]