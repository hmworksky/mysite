from django.conf.urls import url
from automated_testing import create_case
urlpatterns = [
    url(r'^create_case/(\d+)/$',create_case.create_case , name='create_case'),
  ]