from django.urls import path
from . import views

app_name='artist'
urlpatterns= [
    path('key/',views.key, name='key'),
    path('jonghyun/',views.jonghyun, name='jonghyun'),
    path('taemin/',views.taemin, name='taemin'),
    path('onew/',views.onew, name='onew'),
    path('minho/',views.minho, name='minho'),
]