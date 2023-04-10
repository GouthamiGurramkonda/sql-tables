from django.shortcuts import render

# Create your views here.
from app.models import *

def dept(request):
    DO=DEPT.objects.all()
    d={'name':DO}
    return render(request,'dept.html',d)



def emp(request):
    EO=EMPT.objects.all()
    d={'name':EO}
    return render(request,'emp.html',d)
