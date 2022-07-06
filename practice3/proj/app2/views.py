from django.shortcuts import render
from django.http import HttpRequest as req
from django.http import HttpResponse as res
from django.contrib import messages
from .forms import registerform

# Create your views here.
def hello(req1):
    return render(req1,"firsttemplate/hello.html")
def forming(req1):
    form=registerform(req1.POST or None)
    if req1.method=='POST':
        print("Form validated successfully")
        if form.is_valid():
            messages.success(req1,"Success")
            print("Username:",form.cleaned_data['username'])
            print("Roll number:",form.cleaned_data['rollno'])
            print("Email:",form.cleaned_data['email'])
    else:
        print("hello")
        messages.error(req1,"failure")
    return render(req1,"firsttemplate/form.html",{'form':form})
    
    