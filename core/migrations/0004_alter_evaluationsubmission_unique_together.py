# Generated by Django 4.0.1 on 2022-09-15 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evaluation_ended'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluationsubmission',
            unique_together=set(),
        ),
    ]
