"""
URL configuration for wscubeTech project.

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
from django.urls import path
"""from wcube import views   ,   views.function_name krke access krte  h"""
from wcube.views import *
urlpatterns = [
    path("", homepage, name='home'),
    path("about/", about, name='about'),
    path("course/", course, name='course'),
    path("course/<int:courseID>", courseDetails, name='courseid'),     
    path("course/<str:courseID>", courseDetailstr, name='courseid'),
    path("course/<courseID>", coursewithoutType, name='courseid'),
    
    path("aboutAs", aboutAs, name='aboutAs'),
    path("contactAs", contactAs, name='contact'),
    path("serviceAs", serviceAs, name='service'),
    path("userform", userformFun, name='user_form'),
    path("userdetails", UserDetails, name='user_form'),
    
    path("thankyou", thank,name='thankyou'),
    
    path('action', action, name="action"),
    path('submit', submit, name="submitform"),
    
    path('formpy', form_py, name='form'),
    path('calculator', calculator, name="calculator"),
    path('checknum', EvenOdd, name='Check'),
    path('marksheet', marksheet, name='marksheet'),
    
    path('news/<newsId>', newsDetails, name='newsdetails'),
    path('admin/', admin.site.urls),
    
    
]

# name ka use href= {% url 'name' %}  // page link krne me use hota h 
# href = '/aboutAs' dal ke page link kr skte jo aboutAs function me render kiya h
