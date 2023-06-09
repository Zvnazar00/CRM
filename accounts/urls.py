from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),

    path('create_order/', views.CreateOrder, name="create_order"),
    path('update_order/<str:pk>/', views.UpdateOrder, name="update_order"),
    path('update_delete/<str:pk>/', views.deleteOrder, name="delete_order"),

]
