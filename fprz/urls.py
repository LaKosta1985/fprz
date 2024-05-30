
from django.contrib import admin
from django.urls import path,include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from fprz.settings import DEBUG
from django.views.decorators.cache import cache_page


document_patterns=[
    path('document', cache_page(60*3)(Doc_fprz.as_view()),name="doc"),
    path('pologeniya', Pologeniya_fprz.as_view(),name="polog"),
    path('protocol', protocol,name="protocol"),
    path('normativ', normativ,name="norm"),
]

sorev_patterns=[
    path('calendar', calendar,name="calendar"),
    path("zayavka",zayavka,name='zayavka'),
    #path("mailPost",mailPost,name='mailPost'),
    path('albom_foto',albom_foto,name="albom_foto"),
    path('foto/<slug:slug_foto>',foto,name="foto")
    #path('zayvka', views.zayvka,name="zayvka"),
]

sportsmens_patterns=[
    path('feder_member', feder_member,name="feder_member"),
    path('calendar', calendar,name="calendar"),
    path('record', record,name="record"),
]

urlpatterns = [
    path("", cache_page(3)(Main_fprz.as_view()),name='index'),
    path("documents/", include(document_patterns)),
    path('admin/', admin.site.urls,name='admin'),
    #path('search/', Main_fprz,name='search'),
    path('user/', include(('users.urls','users'), namespace='users')),
    path("like/", like,name='like'),
    path("like_/", like_,name='like_'),
    path("contacts",contacts,name='contacts'),
    path("sorev/", include(sorev_patterns)),
    path("sportsmens/", include(sportsmens_patterns)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("anti/", Anti_fprz.as_view(),name='anti'),
    path("captcha/", include('captcha.urls')),
    path('mailPost/<slug:slug_status>',mailPost,name='mailPost'),
]

if DEBUG:
     urlpatterns +=[path("__debug__/", include("debug_toolbar.urls")),]



if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

