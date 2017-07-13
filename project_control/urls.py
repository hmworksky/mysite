from django.conf.urls import url,include
from project_control import views


urlpatterns = [
    url(r'^login/',include('sign.urls')),
    url(r'create/', views.project_create, name ='project_create'),
]