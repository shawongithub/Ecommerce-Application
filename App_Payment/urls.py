from django.urls import path
app_name="App_Payment"
from . import views

urlpatterns=[
    path('checkout/',views.checkout, name="checkout"),
    path('pay/',views.payment, name="payment"),
    path('status/',views.complete, name="complete"),
    path('purchase/<val_id>/<tran_id>',views.purchase, name="purchase"),
    path('orders/',views.order_view,name="orders"),
]