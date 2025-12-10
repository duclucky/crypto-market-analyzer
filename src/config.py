"""Application configuration."""

class Config:
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    API_TIMEOUT = 30
    CACHE_EXPIRY = 3600
    MAX_RETRIES = 3

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
