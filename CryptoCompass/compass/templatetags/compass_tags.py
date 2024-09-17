from django import template

from config import settings
from cmc_api.utils import CMCHTTPClient


register = template.Library()

@register.simple_tag()
def get_coin_list():
    base_url = "https://pro-api.coinmarketcap.com"

    result = CMCHTTPClient(base_url=base_url, api_key=settings.CMC_API_KEY).get_listings()

    return result