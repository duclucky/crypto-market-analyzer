"""Blockchain network data API."""

class BlockchainAPI:
    """Fetch blockchain network metrics."""
    
    def get_network_stats(self, blockchain):
        """Get blockchain statistics."""
        return f"Stats for {blockchain}"
    
    def get_transaction_volume(self, blockchain):
        """Get transaction volume."""
        return f"Volume for {blockchain}"
    
    def get_active_addresses(self, blockchain):
        """Get active addresses count."""
        return f"Active addresses for {blockchain}"
