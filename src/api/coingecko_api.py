"""CoinGecko API integration."""

class CoinGeckoAPI:
    """Wrapper for CoinGecko API."""
    
    BASE_URL = "https://api.coingecko.com/api/v3"
    
    def get_market_data(self, coin_id):
        """Fetch market data for a coin."""
        endpoint = f"{self.BASE_URL}/simple/price"
        return None
    
    def get_trending_coins(self):
        """Get trending coins."""
        pass
