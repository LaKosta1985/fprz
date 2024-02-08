from pyexpat.errors import messages
from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

           # session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            #if session_key:
                #Cart.objects.filter(session_key=session_key).update(user=user)
            #messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
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

            #session_key = request.session.session_key

            if user:
                auth.login(request, user)
                #messages.success(request, f"{username}, Вы вошли в аккаунт")

                #if session_key:
                    #Cart.objects.filter(session_key=session_key).update(user=user)

                #redirect_page = request.POST.get('next', None)
                #if redirect_page and redirect_page != reverse('user:logout'):
                    #return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)

def profile(request):
  
   context= {
      "title": "Main",
   }

   return render(request,'profile.html', context)
   

def logout(request):
  
    #messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('index'))
