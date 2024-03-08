from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import New, Doc, Table_Norm, Table_Cat,Calendar,Table_Record,Table_Cat_Record,Foto,Polog,Protocol
from users.models import User
from django.core.paginator import Paginator
from fprz.utils import q_search
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def index(request):
    # принимаем id блока ленты
    id_ = request.GET.get("nameCount")
    if id_:
        id_new = New.objects.get(id=id_)
        id_new.count_view = id_new.count_view + 1
        id_new.save()

    like_ = request.GET.get("LikeCount")
    if like_:
        id_like = New.objects.get(id=like_)
        id_like.like = id_like.like + 1
        id_like.save()

    page = request.GET.get("page", 1)
    query = request.GET.get("q", None)
    if query:
        news = q_search(query)
    else:
        news = New.objects.all().order_by("-date")
    paginator = Paginator(news, 3)
    current_page = paginator.page(int(page))
    context = {
        "page": current_page,
        "title": "Main",
        "query": query,
    }

    return render(request, "index.html", context)


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


def document(request):
    doc = Doc.objects.all()
    context = {"title": "Документы", "doc": doc}
    return render(request, "document.html", context)


def pologeniya(request):
    doc = Polog.objects.all()
    context = {"title": "Положения", "doc": doc}
    return render(request, "pologeniya.html", context)


def protocol(request):
    doc = Protocol.objects.all()
    context = {"title": "Протоколы", "doc": doc}
    return render(request, "protocol.html", context)


def normativ(request):
    tables = Table_Norm.objects.all()
    categories = Table_Cat.objects.all()
    context = {"title": "Нормативы", "tables": tables, "categories": categories}
    return render(request, "normativ.html", context)


def contacts(request):
    users = User.objects.all()
    context = {"title": "Контакты", "users": users}
    return render(request, "contacts.html", context)

def calendar(request):
    calendar = Calendar.objects.all()
    context = {"title": "Календарь", "calendar": calendar}
    return render(request, "calendar.html", context)


def feder_member(request):
    users = User.objects.all()
    context = {"title": "Нормативы","users": users}
    return render(request, "federmembers.html", context)

def record(request):
    tables = Table_Record.objects.all()
    categories = Table_Cat_Record.objects.all()
    context = {"title": "Рекорды Рязанской области", "tables": tables, "categories": categories}
    return render(request, "record.html", context)





def zayavkaPost(request):
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
   msg=EmailMultiAlternatives(subject="письмо с сайта РФП(fprz.ru)",from_email="fprz62@yandex.ru",to=["xxxascent@rambler.ru",])
   msg.attach_alternative(email_body,"text/html")
   msg.send()
   return render(request,"zayavka.html",context=data)


def zayavkaGet(request):
   return render(request,"zayavka.html")


def albom_foto(request):
    albom = Foto.objects.all()
    if  albom:
        context = {"title": "Альбом соревнований","albom": albom}
        return render(request, "albom_foto.html", context)
    else:
        return render(request, "albom_foto.html")
    

def anti(request):
  
        return render(request, "anti.html")