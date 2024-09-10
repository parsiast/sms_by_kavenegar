from django.urls import path 
from smsapp import views

urlpatterns = [
    path('',views.sms,name='smsview'),
    path('usms/<int:user_id>',views.smssender)]