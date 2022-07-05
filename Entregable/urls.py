"""Entregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Entregable.views import saludo, template
from AppEntregable.views import padre, madre, hermano, template1, templateHermano, templateMadre, templatePadre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('template', template),
    path('padre/', padre), 
    path('madre/', madre),
    path('hermano/', hermano),
    path('template1/', template1),
    path('template_hermano/', templateHermano),
    path('template_madre/', templateMadre),
    path('template_padre/', templatePadre),

]
