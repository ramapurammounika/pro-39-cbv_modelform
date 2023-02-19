from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django. http import HttpResponse
from django.views.generic import *


def fbv_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}

    if request.method=='POST':
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webpage is inserted by using Model Forms')
    return render(request,'fbv_modelform.html',d)


class cbv_modelform(View):
    def get(self,request):
        WFO=ModelWebpageForm()
        d={'form':WFO}
        return render(request,'cbv_modelform.html',d)

    def post(self,request):
        WFD=ModelWebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('data is inserted successfully')