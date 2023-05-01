from django.urls import path

from app1.views import *

app_name='seshu'

urlpatterns=[
    path('specifi_url/',specifi_url,name='specifi_url'),
]