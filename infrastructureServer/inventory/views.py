from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def newstock(request):
    return render(request,"newstock.html")

def statistics(request):
    return render(request,"statistics.html")