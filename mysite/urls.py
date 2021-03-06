"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',include('sign.urls')),
    url(r'^http/'  , include('http_tool.urls')),
    url(r'^interface/',include('interface_control.urls')),
    url(r'^index/',include('home.urls')),
    url(r'^project/',include('project_control.urls')),
    url(r'^env/',include('env_config.urls')),
    # url(r'^data/',include('data_center.urls')),
    url(r'^auto/',include('automated_testing.urls')),

]
