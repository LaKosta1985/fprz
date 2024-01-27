from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models  import New
def index(request):
   news=New.objects.all()
   return render(request,'index.html',context={"sportsmen":news,'title':'Main'})
   
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