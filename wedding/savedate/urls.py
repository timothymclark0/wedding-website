from django.urls import path
from .views import *

app_name = 'savedate'

urlpatterns = [
    #path('registry', registry, name='registry'),
    path('',savethedate,name ='savethedate'),
    path('<str:page>',notion_page, name= 'notion'),
    
]