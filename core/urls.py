from django.urls import path, include
from .views import *
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', api_views.ItemModelViewSet, basename='items')
router.register('users', api_views.UserModelViewSet, basename='users')


app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('products/', ProductsView.as_view(), name='products'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<int:pk>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<int:pk>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('testpayment/', PaymentTestView.as_view(), name='payment_test'),
    path('request-refund/<slug:ref_code>',
         RequestRefundView.as_view(), name='request-refund'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('api/', include(router.urls)),
]
#     path('shirts/', HomeShirtView.as_view(), name='home_shirt'),
#     path('sports/', HomeSportView.as_view(), name='home_sports'),
#     path('casuals/', HomeCasualView.as_view(), name='home_casuals'),
