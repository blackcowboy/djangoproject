"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from pathlib import Path
from admin_custom_view import CustomRsaAdminLoginView

urlpatterns = [
    path("admin/login/", CustomRsaAdminLoginView.as_view(), name="admin_login"),
    path('admin/', admin.site.urls),
    # path('demo/', include('apps.demo.urls'))
]


BASE_DIR = Path(__file__).resolve().parent.parent
for a in (BASE_DIR / 'apps').iterdir():
    urlpatterns.append(path(a.name + '/', include('apps.' + a.name + '.urls')))
