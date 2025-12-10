"""Price analysis module."""

class PriceAnalyzer:
    """Analyze cryptocurrency prices."""
    
    def __init__(self):
        self.coins = ['bitcoin', 'ethereum', 'cardano']
    
    def get_current_price(self, coin):
        """Get current price of a coin."""
        return f"Fetching price for {coin}"
    
    def calculate_change(self, coin, period=7):
        """Calculate price change over period."""
        return f"Price change for {coin} over {period} days"
