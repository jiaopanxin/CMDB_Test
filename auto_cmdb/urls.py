"""auto_cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from extra_apps import xadmin
from auto_cmdb.settings import MEDIA_ROOT
from django.views.static import serve
from .views import DashView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index2.html'),name="index"),
    path('users/', include('users.urls')),
    path('cmdb/', include('cmdb.urls')),
    path('octoups/', include('octoups.urls'),name="octoups"),
    path('api/', include('api.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('dash/',DashView.as_view()),

    path('aa/',TemplateView.as_view(template_name="octoups/connection.html"))
]
