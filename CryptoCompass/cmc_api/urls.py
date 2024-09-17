from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('coinlist/', cache_page(30)(views.CoinAPIList.as_view())),
    path('coinlist/<slug:currency_slug>/', cache_page(30)(views.CurrencyAPI.as_view())),
]
