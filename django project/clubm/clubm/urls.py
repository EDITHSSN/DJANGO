"""clubm URL Configuration

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
from club.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guest/', home),
    path('guest/login/', login),
    path('guest/login/signup/', signup ),
    path('guest/login/profile/', profile),
    path('guest/club/', club),
    path('guest/signup/details/', details),
    path('guest/test/', test),
    path('guest/login/profile/event/', eventt),
    path('guest/login/editor_profile/', editor_profile),
    path('guest/login/editor/pevent/', pevent),
    path('guest/login/forgotp/',forgotp),
    path('guest/login/change_password/',change_password),
    path('guest/club_page/',club_page),
    path('guest/profile/chat/',chat),
]
