"""a URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app import views
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.list_page,name = 'list'),
    url(r'^gy/$',views.gy_page,name = 'gy'),
    url(r'^photo/$',views.photo_page,name = 'photo'),
    url(r'^day/$',views.day_page,name = 'day'),
    url(r'^gd/$',views.gd_page,name = 'gd'),
    url(r'^dt/$',views.dt_page,name = 'dt'),
    url(r'^xx/$',views.xx_page,name = 'xx'),
    url(r'^blog/$',views.blog_page,name = 'blog'),
]

