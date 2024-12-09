from django.db import models

# Create your models here.
class JobSeeker(models.Model):
    name = models.CharField(max_length=100) 
    mobileNumber =  models.IntegerField()
    email = models.EmailField()
    description = models.CharField(max_length=255)

class Expertise(models.Model):
   description = models.CharField(max_length=255)
   jobSeekerId = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='expertises')

class KeySkill(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=1000,null=True)
    jobSeekerId = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='KeySkills')


class Experience(models.Model):
     companyName = models.CharField(max_length=100,null=True)
     projectName = models.CharField(max_length=1000,null=True)    
     startFrom  = models.DateTimeField(null=True)
     endTo = models.DateTimeField(null=True)
     clientName = models.CharField(max_length=1000,null=True)
     Designation = models.CharField(max_length=100,null=True)
     jobSeekerId = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='Experiences',null=True)

     
class ProjectDescription(models.Model):
     description = models.CharField(max_length=255,null=True)
     expeienceId = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='ProjectDescriptions',null=True)