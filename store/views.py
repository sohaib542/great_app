from django.shortcuts import render

# Create your views here.

def store(request):
    return (request,'store/store.html')