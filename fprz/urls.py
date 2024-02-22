"""
URL configuration for fprz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from fprz.settings import DEBUG
import debug_toolbar

document_patterns=[
    path('document', views.document,name="doc"),
    path('pologeniya', views.pologeniya,name="polog"),
    path('normativ', views.normativ,name="norm"),
]

urlpatterns = [
    path("", views.index,name='index'),
    path("documents/", include(document_patterns)),
    path('admin/', admin.site.urls,name='admin'),
    path('search/', views.index,name='search'),
    path('user/', include(('users.urls','users'), namespace='users')),
    path("like/", views.like,name='like'),
    path("like_/", views.like_,name='like_'),
    path("contacts",views.contacts,name='contacts'),
    
]

if DEBUG:
     urlpatterns +=[path("__debug__/", include("debug_toolbar.urls")),]



if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
sport_patterns=[
    path('autorize', views.autorize),
    path('federMember', views.federMember),
    path('record', views.record),
    path('create_sport', views.create_sport),
    path('create_sport_post', views.create_sport_post),
    path("edit_sport/<int:id>/", views.edit_sport),
    path("delete_sport/<int:id>/", views.delete_sport),
]

sorev_patterns=[
    path('calendar', views.calendar),
    path('protocol', views.protocol),
    path('foto', views.foto),
    path('zayavka', views.zayavka),
]

document_patterns=[
    path('document', views.document),
    path('pologeniya', views.pologeniya),
    path('normativ', views.normativ),
]

urlpatterns = [
     path("", views.index,name='index'),
   
     path("set", views.set),
     path("sportsmens/", include(sport_patterns)),
     path("sorev/", include(sorev_patterns)),
     path("documents/", include(document_patterns)),
     path("antiDop", views.antiDop),
     path("contacts", views.contacts),
     path("zayavka",views.zayavkaGet),
     path("zayavkaPost",views.zayavkaPost),
     path("admin",views.admin),
     path("test/",views.test)
     
]
'''