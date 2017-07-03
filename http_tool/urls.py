from django.conf.urls import url,include
from http_tool import http_get,http_post
urlpatterns = [
    url(r'^get/list/',http_get.get_list,name='get_list'),
    url(r'^get/create/',http_get.get_create,name='get_create'),
    url(r'^post/list/',http_post.post_list,name='get_list'),
    url(r'^post/create/',http_post.post_create,name='post_create'),
  ]

