# Generated by Django 4.0.1 on 2022-09-11 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student Profile'},
        ),
    ]
