from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def index(request):
   #sportsmen=Sportsmen.objects.all()
   #return render(request,"index.html",context={"sportsmen":sportsmen})
   context={
      'title':'Main',
      'content':'qeerqwe'
   }
   return render(request,'index.html',context)
   
def document(request):
   #sportsmen=Sportsmen.objects.all()
   #return render(request,"index.html",context={"sportsmen":sportsmen})
   context={
      'title':'Документы',
      'content':'qeerqwe'
   }
   return render(request,'document.html',context)
def pologeniya(request):
   #sportsmen=Sportsmen.objects.all()
   #return render(request,"index.html",context={"sportsmen":sportsmen})
   context={
      'title':'Положения',
      'content':'qeerqwe'
   }
   return render(request,'pologeniya.html',context)
def normativ(request):
   #sportsmen=Sportsmen.objects.all()
   #return render(request,"index.html",context={"sportsmen":sportsmen})
   context={
      'title':'Нормативы',
      'content':'qeerqwe'
   }
   return render(request,'normativ.html',context)