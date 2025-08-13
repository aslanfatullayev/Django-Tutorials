from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

def uzbekistan(request):
    return render(request, 'pages/uzbekistan.html')

def jahon(request):
    return render(request, 'pages/jahon.html')
