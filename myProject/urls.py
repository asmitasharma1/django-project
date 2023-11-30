# from myApp import views
from django.contrib import admin
from django.urls import path, include
from myApp.views import userlogin 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', userlogin, name='userlogin'),
    
    path('myApp/',include('myApp.urls')),  
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)