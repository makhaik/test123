# Generated by Django 5.1.3 on 2024-11-29 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_rename_student_jobseeker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('jobSeekerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expertises', to='myApp.jobseeker')),
            ],
        ),
    ]
