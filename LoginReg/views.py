from django.shortcuts import render, HttpResponseRedirect
from LoginReg.models import Reg
from LoginReg.forms import RegForm
from LoginReg.forms import LoginForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=RegForm()
    return render(request,'home.html',{'form':form})

def login(request):
    if request.method == "POST":
        form1=LoginForm(request.POST)
        if form1.is_valid():
            user = form1.cleaned_data['User']
            password = form1.cleaned_data['Password']
            dbuser=Reg.objects.filter(user=user,pwd=password)
            if not dbuser:
                return HttpResponse("Failed")
            else:
                return HttpResponse("Hello")


    else:
        form1=LoginForm()
    return render(request,'login.html',{'form1':form1})
