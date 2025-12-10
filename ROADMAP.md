
## Examples

### Getting Price Data
\\\python
from src.analyzers.price_analyzer import PriceAnalyzer
analyzer = PriceAnalyzer()
price = analyzer.get_current_price('bitcoin')
\\\

### Portfolio Tracking
\\\python
from src.portfolio.tracker import PortfolioTracker
tracker = PortfolioTracker()
tracker.add_holding('bitcoin', 0.5, 45000)
\\\
"@ | Add-Content README.md
git add README.md
git commit -m "docs: Add usage examples to README"

# COMMIT 24: Roadmap
Write-Host "📝 COMMIT 24: Roadmap..." -ForegroundColor Green
@"
# Project Roadmap

## Q1 2025
- [x] Project setup and structure
- [x] Core analyzer modules
- [x] API integrations

## Q2 2025
- [ ] Web dashboard
- [ ] Real-time data streaming
