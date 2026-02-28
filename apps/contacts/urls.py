from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list_view, name='contact_list'),
    path('new/', views.contact_form_view, name='contact_create'),
    path('send/', views.send_money_view, name='send_money'),
]
