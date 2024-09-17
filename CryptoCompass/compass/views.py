from django.shortcuts import render
from django.views.generic import View, TemplateView

from config import settings
from cmc_api.utils import CMCHTTPClient

class CoinListView(TemplateView):
    template_name = "compass/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "CryptoCompass"
        return context
    
class CurrencyView(View):
    def get(self, request, currency_slug:str):
        base_url = "https://pro-api.coinmarketcap.com"
        response = CMCHTTPClient(base_url=base_url, api_key=settings.CMC_API_KEY).get_currency(currency_slug=currency_slug)
        
        result = [res for res in response["data"].values()][0]
        return render(request, 'compass/currency.html', {'title': currency_slug.capitalize(), 'coin': result})

        