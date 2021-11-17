
from django.http import response
from django.shortcuts import render
import requests
from .models import Feature

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
        word=request.GET['text']
        api="https://api.dictionaryapi.dev/api/v2/entries/en/"
        a=word
        feature1=Feature()
        feature1.name=Feature(name=a)
        feature1.name.save()
        response=requests.get(api+a).json

        return render(request,'search.html',{'words':response})

def recent(request):
    data=Feature.objects.all()
    return render (request,'recent.html',{'value':data})

  