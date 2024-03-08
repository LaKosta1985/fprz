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
    path('protocol', views.protocol,name="protocol"),
    path('normativ', views.normativ,name="norm"),
]

sorev_patterns=[
    path('calendar', views.calendar,name="calendar"),
    path("zayavka",views.zayavkaGet,name='zayavkaGet'),
    path("zayavkaPost",views.zayavkaPost,name='zayavkaPost'),
    #path('protocol', views.protocol,name="protocol"),
    path('albom_foto', views.albom_foto,name="albom_foto"),
    #path('zayvka', views.zayvka,name="zayvka"),
]

sportsmens_patterns=[
    path('feder_member', views.feder_member,name="feder_member"),
    path('calendar', views.calendar,name="calendar"),
    path('record', views.record,name="record"),
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
    path("sorev/", include(sorev_patterns)),
    path("sportsmens/", include(sportsmens_patterns)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("anti/", views.anti,name='anti'),
]

if DEBUG:
     urlpatterns +=[path("__debug__/", include("debug_toolbar.urls")),]



if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

