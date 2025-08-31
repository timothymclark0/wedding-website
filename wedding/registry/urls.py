from django.urls import path
from .views import *

app_name = 'registry'

urlpatterns = [
    path('',registry,name ='registry'),
    path('/?=<',registry,name ='registry'),
    path('gift/<str:slug>', gift_page, name='gift_page'),
    path('gift/<str:slug>/claim', claim_gift, name='claim_gift')
]