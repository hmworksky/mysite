from django.conf.urls import url,include
from http_tool import http_get,http_post,encryption,translation,mySocket
urlpatterns = [
    url(r'^get/list/',http_get.get_list,name='get_list'),
    url(r'^get/create/',http_get.get_create,name='get_create'),
    url(r'^post/list/',http_post.post_list,name='get_list'),
    url(r'^post/create/',http_post.post_create,name='post_create'),
    url(r'^get/detail/(\d+)/$',http_get.get_detail,name='get_detail'),
    url(r'^post/detail/(\d+)/$',http_post.post_detail,name='post_detail'),
    url(r'^get/edit/(\d+)/$',http_get.get_edit,name='get_edit'),
    url(r'^post/edit/(\d+)/$',http_post.post_edit,name='post_edit'),
    url(r'^get/delete/(\d+)/$',http_get.get_delete,name='get_delete'),
    url(r'^post/delete/(\d+)/$',http_post.post_delete,name='post_delete'),
    url(r'^encryption/$',encryption.encry_base64,name='encry_base64'),
    url(r'^translation/$',translation.viewTranslation,name='viewTranslation'),
    url(r'^get_translation_result/$',translation.getTranslationResult,name='getTranslationResult'),
    url(r'^echo$',mySocket.echo,name='echo'),
    url(r'^shutdown',http_post.shutdown,name='shutdown'),
  ]

