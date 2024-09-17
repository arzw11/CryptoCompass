from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from config import settings
from .utils import CMCHTTPClient


class CoinAPIList(APIView):
    def get(self, request):
        base_url = "https://pro-api.coinmarketcap.com"
        result = CMCHTTPClient(base_url=base_url, api_key=settings.CMC_API_KEY).get_listings()

        return Response(data=result, status=status.HTTP_200_OK)

class CurrencyAPI(APIView):
    def get(self, request, currency_slug):
        base_url = "https://pro-api.coinmarketcap.com"
        result = CMCHTTPClient(base_url=base_url, api_key=settings.CMC_API_KEY).get_currency(currency_slug=currency_slug)

        return Response(data=result["data"], status=status.HTTP_200_OK)