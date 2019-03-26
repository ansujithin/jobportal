from django.shortcuts import render
from testApp.models import Jobs

# Create your views here.
def home(request):
    return render(request,'testApp/home.html')
def jobs(request):
    jobs_list=Jobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/jobs.html',context=my_dict)
