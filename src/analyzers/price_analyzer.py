"""Price analysis module."""

class PriceAnalyzer:
    """Analyze cryptocurrency prices."""
    
    def __init__(self):
        self.coins = ['bitcoin', 'ethereum', 'cardano']
    
    def get_current_price(self, coin):
        return f"Fetching price for {coin}"
