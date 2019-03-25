from django.shortcuts import render
from testapp.models import hydjobs,bangalorejobs,chennaijobs,keralajobs,punejobs
from . import forms
# Create your views here.

def hydjobs(request):
    job_list=hydjobs.objects.order_by('date')
    my_dict={'job_list':job_list}
    return render(request,'testapp/hybdjobs.html',context=my_dict)
def bangalorejobs(request):
    job_list=bangalorejobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/bangalorejobs.html',context=my_dict)
def chennaijobs(request):
    job_list=chennaijobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)
def keralajobs(request):
    job_list=keralajobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/keralajobs.html',context=my_dict)
def punejobs(request):
    job_list=punejobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/pune.html',context=my_dict)
def greeting_view(request):
    return render(request,'testapp/thankyou.html')
def feedback_view(request):
    if request.method=="GET":
        form=forms.FeedBackForm()
        '''return render(request,'testapp/contactus.html',{'form':form})'''
    if request.method == "POST":
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("data entered sucessfully")
            print("the name is:",form.cleaned_data["name"])
            print("the email is:",form.cleaned_data["email"])
            
            print("the message is:",form.cleaned_data["message"])
            '''return greeting_view(request)'''

    return render(request,'testapp/contactus.html',{'form':form})
