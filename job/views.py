from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    job_list = Job.objects.all() # Fitch all data from Job model
    context = {'jobs': job_list} # name of data that fitch in template
    return render(request, 'job/job_list.html', context)

def job_detail(request, id):    
    job_detail = Job.objects.get(id=id) # get the single job by id
    context = {'job':job_detail} # The name we use in template 
    return render(request, 'job/job_detail.html', context)