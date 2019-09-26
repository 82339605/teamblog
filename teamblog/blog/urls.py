from django.conf.urls import url,include
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^$',index_views),
    url(r'register/',register,name='register'),
    url(r'login/',login,name='login'),
    url(r'check_repeat/',check,name='check'),
    url(r'logout/',logout,name='logout'),
    url(r'publish/',publish,name='publish'),
    url(r'info1/',info,name='info0'),
    url(r'info2/',info2,name='info1'),
    url(r'info3/',info3,name='info3'),
    url(r'leave/',leave,name='leave'),
    url(r'text/',text,name='text'),
    url(r'aboutMy/',aboutmy,name='aboutMy'),
    url(r'note/',note,name='note'),
    url(r'note1/',note1,name='note1'),
    url(r'note2/',note2,name='note2'),
    url(r'note3/',note3,name='note3'),
    url(r'time/',time,name='time'),
    url(r'luanting/',luanting,name='luanting'),
    url(r'tarena/',tarena,name='tarena'),
    url(r'checkPow/',checkPow,name='checkPow'),
    url(r'about/',about,name='about')
]