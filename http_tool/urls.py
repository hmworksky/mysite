from django.conf.urls import url,include
from http_tool import views
urlpatterns = [
      url(r'^get/',views.http_get,name='http_get'),
  ]

