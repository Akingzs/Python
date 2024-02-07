from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'global\index.html')

def page1(request):
    return HttpResponse('page 1')

# usando render 
def page2(request):
    return render(request, 'home\page2.html')
# usando render 
def page3(request):
    return render(request, 'home\page3.html')