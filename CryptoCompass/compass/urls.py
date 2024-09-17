from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('',cache_page(180)(views.CoinListView.as_view())),
    path('currencies/<slug:currency_slug>/', cache_page(30)(views.CurrencyView.as_view()), name="currency")
]
