# Generated by Django 3.2.13 on 2022-12-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='key',
            field=models.CharField(default='', max_length=35, verbose_name='패스워드 키'),
        ),
    ]
