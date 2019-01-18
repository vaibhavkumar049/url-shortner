from django.urls import path
from . import views

urlpatterns=[
    path('',views.url_new,name='url_list'),
    path('detail/<int:pk>',views.url_list,name='url_detail'),
    path('<str:key>',views.redirect_to_website,name='redirect_to_Website')
]