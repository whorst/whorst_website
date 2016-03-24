from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^projects$',views.projects, name = 'projects'),
    url(r'^coursework$',views.projects, name = 'coursework'),
    url(r'^home$', views.home, name='home'),
    url(r'^hobbies$', views.hobbies, name='hobbies'),
    url(r'^contact$', views.contact, name='contact'),
    #url(r'^$', views.projects, name='projects'),
    #The above code will look for views named home
]
#localhost:8000/home