from django.urls import path
from form import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('counselling/', views.counselling, name='counselling'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('btech/', views.btech, name='btech'),
    path('btech1/', views.btech1, name='btech1'),
    path('btech2/', views.btech2, name='btech2'),
    path('btech3/', views.btech3, name='btech3'),
    path('btech4/', views.btech4, name='btech4'),
    path('btech5/', views.btech5, name='btech5'),
    path('btech6/', views.btech6, name='btech6'),
    path('btech7/', views.btech7, name='btech7'),      
    path('btech-edit/', views.btech_edit, name='btech_edit'),
    path('btech-preview/', views.btech_preview, name='btech_preview'),
    path('btechle/', views.btechle, name='btechle'),
    path('btechle1/', views.btechle1, name='btechle1'),
    path('btechle2/', views.btechle2, name='btechle2'),
    path('btechle3/', views.btechle3, name='btechle3'),
    path('btechle4/', views.btechle4, name='btechle4'),
    path('btechle5/', views.btechle5, name='btechle5'),
    path('btechle6/', views.btechle6, name='btechle6'),
    path('btechle7/', views.btechle7, name='btechle7'),      
    path('btechle-edit/', views.btechle_edit, name='btechle_edit'),
    path('btechle-preview/', views.btechle_preview, name='btechle_preview'),
    path('bba/', views.bba, name='bba'),
    path('bba1/', views.bba1, name='bba1'),
    path('bba2/', views.bba2, name='bba2'),
    path('bba3/', views.bba3, name='bba3'),
    path('bba4/', views.bba4, name='bba4'),
    path('bba5/', views.bba5, name='bba5'),
    path('bba6/', views.bba6, name='bba6'),      
    path('bba-edit/', views.bba_edit, name='bba_edit'),
    path('bba-preview/', views.bba_preview, name='bba_preview'),
    path('mba/', views.mba, name='mba'),
    path('mba1/', views.mba1, name='mba1'),
    path('mba2/', views.mba2, name='mba2'),
    path('mba3/', views.mba3, name='mba3'),
    path('mba4/', views.mba4, name='mba4'),
    path('mba5/', views.mba5, name='mba5'),
    path('mba6/', views.mba6, name='mba6'),  
    path('mba-edit/', views.mba_edit, name='mba_edit'),    
    path('mba-preview/', views.mba_preview, name='mba_preview'),
]

urlpatterns += staticfiles_urlpatterns()


# path('pdfs/', views.pdfs, name='pdfs'),   
# we dont need a pdf view because 'pdfs/' shall only be accesible to admin and not to normal users