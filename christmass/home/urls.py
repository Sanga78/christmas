from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('send_message/<str:username>/',views.message,name='message')
]