from django.conf.urls import url
from automated_testing import create_case,case_info
urlpatterns = [
    url(r'^create_case/(\d+)/$',create_case.create_case , name='create_case'),
    url(r'^case_info/$',case_info.case_info , name='case_info'),
    url(r'^queue/$',case_info.case_queue , name='case_queue'),
  ]