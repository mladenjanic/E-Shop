from django.urls import path

from .views import (HomeView, ItemDetailView, add_to_cart, products, remove_from_cart, OrderSummaryView, remove_single_item_from_cart, add_single_item_to_cart, CheckoutView, PaymentView)

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('add-single-item-to-cart/<slug>/', add_single_item_to_cart, name='add-single-item-to-cart'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
]
