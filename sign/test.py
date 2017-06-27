from django.conf import settings
from tools import *
from models import *
#import os
#os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})
def ttt():
    p = InterfaceInfo.objects.all()
    print p
if __name__ == '__main__' :
    ttt()

