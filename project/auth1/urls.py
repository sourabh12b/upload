from django.urls import path
from  . import views

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login',views.log_in,name='log'),
    path('log',views.log_out,name='logout')
]
