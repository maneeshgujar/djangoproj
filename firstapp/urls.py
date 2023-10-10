from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainfunc),
    path('first/',views.func),
    path('members/',views.memfunc, name='allmembers'),
    path('members/details/<int:id>',views.detailsfunc),
]