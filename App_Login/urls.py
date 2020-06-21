from django.urls import path

app_name='App_Login'
from App_Login import views

urlpatterns = [
   path('signup/',views.sign_up,name='signup'),
   path('login/',views.login__user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('profile/',views.user_profile,name='profile'),
]
