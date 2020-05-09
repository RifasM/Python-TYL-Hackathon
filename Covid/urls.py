"""Covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import Covid.views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name="home"),
    path('positive', view.positive, name="positive"),
    path('negative', view.negative, name="negative"),
    path('deaths', view.deaths, name="deaths"),
    path('isolation', view.isolation, name="isolation"),
    path('district', view.district, name="district"),
    path('discharged', view.discharged, name="discharged"),
    path('ward', view.wards, name="wards"),
]
