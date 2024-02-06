from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models  import New
from django.core.paginator import Paginator
def index(request):
   page=request.GET.get('page',1)
   news=New.objects.all()
   paginator=Paginator(news,2)
   current_page=paginator.page(int(page))
   context= {
      "page": current_page,
      "title": "Main",
   }

   return render(request,'index.html', context)
   






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