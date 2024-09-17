from requests import Session

class HTTPClient:
    
    def __init__(self, base_url:str, api_key:str):
        self.base_url = base_url
        self.api_key = api_key
        

class CMCHTTPClient(HTTPClient):
    def get_listings(self):
        with Session() as session:
            response = session.get(
                url=self.base_url+"/v1/cryptocurrency/listings/latest",
                headers={
                    'X-CMC_PRO_API_KEY': self.api_key,
                }
            )
            result = response.json()

            return result["data"]
    
    def get_currency(self, currency_slug: str):
        with Session() as session:
            response = session.get(
                url=self.base_url+"/v2/cryptocurrency/quotes/latest",
                headers={
                    'X-CMC_PRO_API_KEY': self.api_key,
                },
                params={
                    'slug': currency_slug,
                }
                                   )
            result = response.json()

            return result

        