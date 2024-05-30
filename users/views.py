
from django.contrib.auth.decorators import login_required
from django.contrib import auth,messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from PIL import Image
from users.forms import *
from django.views.generic import ListView,DetailView,CreateView
from fprz.settings import FROM_EMAIL_SERVER
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            user = form.instance
            auth.login(request, user)

            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'registration.html', context)



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
           
            user = auth.authenticate(username=username, password=password)

           
            if user:
                
                auth.login(request,user)
             
                messages.success(request, f"{username}, Вы вошли в аккаунт")


                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)




@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            if request.FILES:
                filename = request.FILES['image'].name
                print("filename")
                print(filename)
                img = Image.open("load/users/"+filename) # Open image using self
                if img.height > 1200 or img.width > 1200:
                    new_img = (1200, 700)
                    img.thumbnail(new_img)
                    img.save("load/users/"+filename)  # saving image at the same path
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
        

        context = {
            'title': 'Home - Кабинет',
            'form': form
       
        }
    return render(request, 'profile.html', context)

   




@login_required
def logout(request):
  
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('index'))

def sendMesToEmail(request): 
   if request.method=='POST': 
        form=SendPassToEmail(request.POST)
        if form.is_valid():
                try:
                    mail=request.POST.get("email")
                    user=User.objects.filter(email=mail)
                    if user:
                        for i in user:
                            email_body=i.password
                        print(email_body)
                        if mail:
                             msg=EmailMultiAlternatives(subject="Пароль профиля сайта РФП(fprz.ru)",from_email=FROM_EMAIL_SERVER,to=[mail,])
                             msg.attach_alternative(email_body,"text/html")
                             msg.send()
                             return render(request, "login.html",{'form':form,'title':"Пароль",'data':mail}) 
                    else:
                        form.add_error(None,"Такой Email не зарегистрирован")      
                except:
                    form.add_error(None,"Ошибка при отправлении(") 
   else:
       form=SendPassToEmail()       
   return render(request, "sendMesToEmail.html",{'form':form,'title':"Пароль"}) 