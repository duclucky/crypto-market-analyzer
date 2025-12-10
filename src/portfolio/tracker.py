"""Portfolio tracking functionality."""

class PortfolioTracker:
    """Track cryptocurrency holdings and performance."""
    
    def __init__(self):
        self.holdings = {}
    
    def add_holding(self, coin, amount, buy_price):
        """Add a coin holding to portfolio."""
        self.holdings[coin] = {
            'amount': amount,
            'buy_price': buy_price
        }
    
    def remove_holding(self, coin):
        """Remove a coin from portfolio."""
        if coin in self.holdings:
            del self.holdings[coin]
    
    def calculate_portfolio_value(self):
        """Calculate total portfolio value."""
        return sum(h['amount'] * h['buy_price'] for h in self.holdings.values())
    
    def get_performance_metrics(self):
        """Get portfolio performance metrics."""
        return {'total_value': self.calculate_portfolio_value()}
