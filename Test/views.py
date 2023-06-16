from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')

def home(request):
    return render(request,'home.html')
def registration(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')