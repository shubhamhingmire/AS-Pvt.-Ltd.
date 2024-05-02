from django.shortcuts import render
from web.models import Data,Founder,Contact,Job,Apply
# Create your views here.
def index(request):
    data=Data.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})

def about(request):
    founderdata=Founder.objects.all()
    
    return render(request,'about.html',{'founderdata':founderdata})

def contact(request):
    
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        mnumber=request.POST.get('mnumber')
        msg=request.POST.get('msg')

        condata=Contact(email=email,name=name,mnumber=mnumber,msg=msg)
        condata.save()
        
    return render(request,'contact.html')

def jobs(request):
    jobdata=Job.objects.all()
    return render(request,'jobs.html',{'jobdata':jobdata})

def apply(request):
    
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        mnumber=request.POST.get('mnumber')
        # resume=request.FILES.get("resume")

        applydata=Apply(email=email,name=name,mnumber=mnumber)
        applydata.save()
    
    return render(request,'apply.html')