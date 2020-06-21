from django.urls import path

app_name='App_Shop'

from App_Shop import views
urlpatterns = [
   path('',views.Home.as_view(),name='home'),
   path('product/<pk>/',views.ProductDetail.as_view(),name='product'),
]
