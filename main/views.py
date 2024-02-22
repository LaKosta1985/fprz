from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models  import New,Doc
from users.models  import User
from django.core.paginator import Paginator
from fprz.utils import q_search
def index(request):
   #принимаем id блока ленты
   id_=request.GET.get('nameCount')
   if id_:
      id_new = New.objects.get(id=id_)
      id_new.count_view=id_new.count_view+1
      id_new.save()
   
   like_=request.GET.get('LikeCount')
   if like_:
      id_like = New.objects.get(id=like_)
      id_like.like=id_like.like+1
      id_like.save()

   page=request.GET.get('page',1)
   query=request.GET.get('q',None)
   if query:
      news=q_search(query)
   else:
      news=New.objects.all()
   paginator=Paginator(news,2)
   current_page=paginator.page(int(page))
   context= {
      "page": current_page,
      "title": "Main",
       "query":query,
   }

   return render(request,'index.html', context)
   

def like(request):

   like_=request.GET.get('LikeCount')
   if like_:
      id_like = New.objects.get(id=like_)
      id_like.like=id_like.like+1
      id_like.save()

   return render(request,'index.html')

def like_(request):

   like_=request.GET.get('LikeCount')
   if like_:
      id_like = New.objects.get(id=like_)
      id_like.like=id_like.like-1
      id_like.save()

   return render(request,'index.html')  


def document(request):
   doc=Doc.objects.all()
   context={
      'title':'Документы',
      'doc':doc
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



def contacts(request):
   users=User.objects.all()

   context={
      'title':'Контакты',
      'users':users
   }
   return render(request,'contacts.html', context)