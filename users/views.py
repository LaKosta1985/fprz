from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def registration(request):
  
   context= {
      "title": "Main",
   }

   return render(request,'registration.html', context)
   

def login(request):
  
   context= {
      "title": "Main",
   }

   return render(request,'login.html', context)

def profile(request):
  
   context= {
      "title": "Main",
   }

   return render(request,'profile.html', context)
   

def logout(request):
  
   context= {
      "title": "Main",
   }

   return render(request,'logout.html', context)
