from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home,name="home"),
    path('shop/',views.shop,name="shop"),
    path('mycart/',views.cart,name="mycart"),
    path('make_payment/',views.make_payment,name="make_payment"),
    path('display/',views.display,name="display"),
    path('contact/',views.contact1,name="contact"),
    path("payment-Status/",views.payment_status,name='payment-status'),
    # admin 
]