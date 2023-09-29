from . import views
from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('about/', views.about, name='about'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('policelogin/', views.policelogin, name='policelogin'),
    path('policedashboard/', views.policedashboard, name='policedashboard'),
    path('signup/', views.signup, name='signup'),
    path('report/', views.report, name='report'),
    path('complaintsuccess/', views.complaintsuccess, name='complaintsuccess'),
    path('mycomplaints/', views.mycomplaints, name='mycomplaints'),    
    path('home/', views.home, name='home'),  
    path('logout/', views.userlogout, name='logout'),
    path('complaints/', views.complaint_list, name='complaint_list'),
    path('policereport/',views.policereport, name='policereport'),
    path('mark_as_solved/<int:complaint_id>/', views.mark_complaint_as_solved, name='mark_complaint_as_solved'),
    path('policelogout/', views.policelogout, name='policelogout'),
    path('', views.home, name='home'),
     re_path(r'^(?P<page>[\w-]+)\.html$', views.html_page, name='html_page'),
    
]
       

