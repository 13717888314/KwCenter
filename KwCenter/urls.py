"""
URL configuration for KwCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include, re_path
# from KwCenter.views.static import serve
# from KwCenter.settings import MEDIA_ROOT
from mycenter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.testPro),
    path('index1/',views.testIndex1),
    path('index2/',views.testIndex2),
    path('index3/',views.testIndex3),
    path('index4/',views.testIndex4),
    path('index5/',views.apipost),
    path('index6/',views.testappid),
    path('index7/',views.testYYid),
    path('index8/',views.tjyy),
]
