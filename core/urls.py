from django.urls import path
from . import views

urlpatterns=[
    path('',views.url_new,name='url_list')
]