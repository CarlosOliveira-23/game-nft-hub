from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.nft_view import NFTViewSet
from .views.transaction_view import TransactionViewSet
from .views.register_view import RegisterView

router = DefaultRouter()
router.register(r'nfts', NFTViewSet, basename='nft')
router.register(r'transactions', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register')
]
