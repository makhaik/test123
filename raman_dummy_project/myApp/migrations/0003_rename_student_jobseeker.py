# Generated by Django 5.1.3 on 2024-11-26 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_rename_jobseeker_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='JobSeeker',
        ),
    ]
