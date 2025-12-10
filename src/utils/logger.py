"""Logging configuration."""

import logging

def setup_logger(name, level=logging.INFO):
    """Configure logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
