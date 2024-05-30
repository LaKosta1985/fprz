from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
from users.models import User
from django.core.paginator import Paginator
from fprz.utils import q_search
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os
from django.conf import settings
from django.views.generic import ListView,DetailView,CreateView
from .forms import *
from fprz.settings import EMAIL_ADRESS,FROM_EMAIL_SERVER,CHOICES_for_mes
import random
from django.db.models import Q

class Main_fprz(ListView):
    paginate_by=3
    model=New
    template_name='index.html'
    def get_queryset(self):
        return New.objects.filter(is_published=True)
    def get_context_data(self, **kwargs):  #передает динамические данные
        context=super().get_context_data(**kwargs)
        context['title']="Главная страница"
        files = os.listdir(os.path.join(settings.PHOTO_URL, 'randomImg')) 
        if (files):
            f=random.choices(files, weights=None, cum_weights=None, k=6)
            context['random_foto']=f
        return context
def like(request):

    like_ = request.GET.get("LikeCount")
    if like_:
        id_like = New.objects.get(id=like_)
        id_like.like = id_like.like + 1
        id_like.save()

    return render(request, "index.html")
def like_(request):

    like_ = request.GET.get("LikeCount")
    if like_:
        id_like = New.objects.get(id=like_)
        id_like.like = id_like.like - 1
        id_like.save()

    return render(request, "index.html")
class Doc_fprz(ListView):
    paginate_by=10
    model=Doc
    template_name='document.html'
    extra_context={'title':'Документы'}
    def get_queryset(self):
        return Doc.objects.filter(is_published=True)
class Pologeniya_fprz(ListView):
    model=Polog
    template_name='pologeniya.html'
    def get_queryset(self):
        return Polog.objects.filter(is_published=True)
    def get_context_data(self, **kwargs):  #передает динамические данные
        context=super().get_context_data(**kwargs)
        context['title']="Положения"
        return context
def protocol(request):
    doc = Protocol.objects.order_by('time_create')
    context = {"title": "Протоколы", "doc": doc}
    return render(request, "protocol.html", context)
def normativ(request):
    tables = Table_Norm.objects.all()
    categories = Table_Cat.objects.all()
    context = {"title": "Нормативы", "tables": tables, "categories": categories}
    return render(request, "normativ.html", context)
def contacts(request):
    users = User.objects.filter(Q(status ='Президент')|Q(status ='Секретарь')|Q(status ='Антидопинговая работа')|Q(status ='Администратор'))
    return render(request, "contacts.html",{'title':"Контакты","users": users})   
def calendar(request):
    calendar = Calendar.objects.order_by('start')
    context = {"title": "Календарь", "calendar": calendar}
    return render(request, "calendar.html", context)
def feder_member(request):
    users = User.objects.all()
    context = {"title": "Члены Федерации", "users": users}
    return render(request, "federmembers.html", context)
class Anti_fprz(ListView):
        paginate_by=3
        model=Anti
        template_name='anti.html'
        def get_queryset(self):
            return Anti.objects.filter(is_published=True)
        def get_context_data(self, **kwargs):  #передает динамические данные
            context=super().get_context_data(**kwargs)
            context['title']="Антидопинг"
            return context
def record(request):
    tables = Table_Record.objects.all()
    categories = Table_Cat_Record.objects.all()
    context = {
        "title": "Рекорды Рязанской области",
        "tables": tables,
        "categories": categories,
    }
    return render(request, "record.html", context)
def zayavka(request):
    if request.method=='POST':
        form =ZayavkaForm(request.POST)
        if form.is_valid():
           try:
                nameSorev=request.POST.get("namesor")
                name=request.POST.get("name")
                lastName=request.POST.get("lastname")
                thirdName=request.POST.get("thirdname")  
                dateBirth=request.POST.get("date")  
                dv=request.POST.get("dv")
                rz=request.POST.get("raz")
                kat=request.POST.get("kat")
                nameTren=request.POST.get("tren")
                mail=request.POST.get("email")
                tel=request.POST.get("tel")
                bestRez=request.POST.get("rez")
                data = {"nameSorev": nameSorev,"name": name,"lastName": lastName,"thirdName": thirdName,
                "dateBirth": dateBirth,"dv": dv,"rz": rz,"kat": kat,"nameTren": nameTren,"mail": mail,"tel": tel,"bestRez": bestRez}
                email_body=render_to_string("email_templates/email_templates.html",data)#передаем данные в шаблон и потом отправляем его
                msg=EmailMultiAlternatives(subject="Заявка с сайта РФП(fprz.ru)",from_email=FROM_EMAIL_SERVER,to=[EMAIL_ADRESS['sekretetar'],])
                msg.attach_alternative(email_body,"text/html")
                msg.send()
                return render(request,"zayavka.html",{'data':data,'form':form,'title':"Заявка"})
           except:
               form.add_error(None,"Ошибка") 
        
    else:
        form=ZayavkaForm()  
    return render(request, "zayavka.html",{'form':form,'title':"Заявка"})  
def mailPost(request,slug_status):
   users = User.objects.all()
   user = User.objects.get(slug=slug_status)
   for_mes=CHOICES_for_mes[user.slug]  
   if request.method=='POST': 
        form=MesForm(request.POST)
        if form.is_valid():
                try:
                    name=request.POST.get("name")
                    mail=request.POST.get("email")
                    text_mes=request.POST.get("text_mes")
                    from_to=user.slug
                    data = {"name": name,"mail": mail,"text_mes":text_mes}
                    email_body=render_to_string("email_templates/mes_templates.html",data)#передаем данные в шаблон и потом отправляем его
                    if from_to:
                            msg=EmailMultiAlternatives(subject="Письмо с сайта РФП(fprz.ru)",from_email=FROM_EMAIL_SERVER,to=[EMAIL_ADRESS[user.slug],])
                            msg.attach_alternative(email_body,"text/html")
                            msg.send()
                            return render(request, "contacts.html",{'data':data,"users":users})         
                except:
                    form.add_error(None,"Ошибка") 
   else:
       form=MesForm()       
   return render(request, "mailPost.html",{'form':form,'users':user,'title':"Сообщение","for_mes":for_mes})         
def albom_foto(request):
    albom = Foto.objects.all()

    if albom:
        context = {"title": "Альбом соревнований", "albom": albom}
        return render(request, "albom_foto.html", context)
    else:
        return render(request, "albom_foto.html")
def foto(request,slug_foto):
    albom = Foto.objects.get(slug=slug_foto)
    files = os.listdir(os.path.join(settings.PHOTO_URL, albom.title,'big')) 
    
    if  albom:
        page = request.GET.get("page", 1)
        paginator = Paginator(files, 5)
        current_page = paginator.page(int(page))
        context = {"paginator": paginator,"page": current_page,"albom": albom}
        return render(request, "foto.html", context)
    else:
        return render(request, "albom_foto.html")

