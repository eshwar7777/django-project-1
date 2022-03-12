from ensurepip import version
from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    return render(request,'users/home.html')



# Create your views here.
