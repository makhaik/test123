from django.shortcuts import render
from .models import JobSeeker,Expertise,KeySkill

def home(request):
    if request.method=='POST':
        fm = request.POST
        jobSeeker = JobSeeker(
                        name=fm.get('firstname')+fm.get('lastname'),
                        mobileNumber=fm.get('mobileNumber'),
                        email=fm.get('email'),
                        description=fm.get('description'))
        jobSeeker.save()
        
        for description in fm.getlist('expertise_descriptions'):
            expertise = Expertise(
            description = description,
            jobSeekerId = jobSeeker
        )
            expertise.save()
            
        for keySkill in fm.getlist('keyskills-tbody'):
                keySkill = KeySkill(
                    title = keySkill.Title,
                    description = keySkill.Description,
                    jobSeekerId = jobSeeker
                )
                keySkill.save()
        
    fm = JobSeeker();
    return render(request, 'myApp/home.html', {'form':fm})
