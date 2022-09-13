"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
# in the path function the first argument is the end point the second is function we want to run and third is the name of the path, we can also put html in the http response in the index or about function this basically does the same thing like routing in express but in a different way 
# basically the django server works like when we hit the runserver command the server comes directly to the urls.py files and check the urls in that files and then routes accoring to those urls we can add as many end points as we want 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index' ),
#     path('about/', views.about, name='about'),
#     path('text/', views.text, name='text')
# ]
# this code is for laying the pipeline
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index' ),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact' ),
    path('analyze/', views.analyze, name='analyze' )
    # path('capfirst', views.capfirst, name='capfirst' ),
    # path('newlineremove', views.newlineremove, name='newlineremove' ),
    # path('spaceremove', views.spaceremove, name='spaceremove' ),
    # path('charcounter', views.charcounter, name='charcounter' )
]
