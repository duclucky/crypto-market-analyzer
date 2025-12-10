"""Tests for price analyzer."""

import pytest
from src.analyzers.price_analyzer import PriceAnalyzer

def test_price_analyzer_init():
    """Test PriceAnalyzer initialization."""
    analyzer = PriceAnalyzer()
    assert analyzer is not None
    assert len(analyzer.coins) > 0

def test_get_current_price():
    """Test getting current price."""
    analyzer = PriceAnalyzer()
    result = analyzer.get_current_price('bitcoin')
    assert 'bitcoin' in result.lower()
