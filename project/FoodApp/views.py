from django.shortcuts import render
from django.http import HttpResponse
from FoodApp.models import Details

# Create your views here.
def welcome(request):
      return HttpResponse("Hello DjangoProject")

def message(request):
      return HttpResponse('<h1> Hello world </h1>')

def home(request):
      return render(request,'FoodApp/home.html')

def register(request):
      return render(request, 'FoodApp/register.html')

def register(request):
      if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            register=Details(username=username,email=email,phone=phone)
            register.save()
      return render(request,'FoodApp/register.html')