from django.urls import path
from . import views

urlpatterns = [
    # path('home', views.home, name="home"),
    path('', views.profile, name="profile"),
    #authentication
    path('register', views.register, name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('otp_verification', views.otp_verification, name="otp_verification"),
   ]