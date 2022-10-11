from django.shortcuts import render
from .views import *
# Create your views here.
def home(request):
    name={'name':'prashanth'}
    return render(request,'app/home.html',name)

def about(request):
    context={'page':'about'}
    return render(request,'app/about.html',context)