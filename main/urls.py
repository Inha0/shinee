from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.index, name="index"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('userlogout', views.userlogout, name="userlogout"),
    path('signup', views.signup, name="signup"),
    path('userdel', views.userdel, name="userdel"),
    path('usermod', views.usermod, name="usermod"),
    path('usermod2', views.usermod2, name="usermod2"),
]