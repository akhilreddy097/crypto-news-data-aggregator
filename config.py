"""
Configuration module for Crypto-News Data Aggregator.

Handles loading and managing application configuration from environment variables.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration class."""

    # Cryptocurrency APIs
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "")
    CCXT_EXCHANGE = os.getenv("CCXT_EXCHANGE", "binance")
    CCXT_API_KEY = os.getenv("CCXT_API_KEY", "")
    CCXT_SECRET = os.getenv("CCXT_SECRET", "")

    # News APIs
    NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
    TAGGED_FEED_URL = os.getenv("TAGGED_FEED_URL", "https://feeds.bloomberg.com/crypto")

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/crypto_news_db")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/crypto_news")
    DB_TYPE = os.getenv("DB_TYPE", "postgresql")

    # Server Configuration
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    SERVER_PORT = int(os.getenv("SERVER_PORT", 5000))
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")

    # Data Collection
    UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 300))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    RETRY_DELAY = int(os.getenv("RETRY_DELAY", 5))

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = os.getenv("LOG_FORMAT", "json")

    # Feature Flags
    ENABLE_CRYPTO_SCRAPING = os.getenv("ENABLE_CRYPTO_SCRAPING", "True").lower() == "true"
    ENABLE_NEWS_SCRAPING = os.getenv("ENABLE_NEWS_SCRAPING", "True").lower() == "true"
    ENABLE_VISUALIZATION = os.getenv("ENABLE_VISUALIZATION", "True").lower() == "true"
    ENABLE_ALERTS = os.getenv("ENABLE_ALERTS", "False").lower() == "true"


class DevelopmentConfig(Config):
    """Development configuration."""
    FLASK_ENV = "development"
    FLASK_DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    FLASK_ENV = "production"
    FLASK_DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DATABASE_URL = "postgresql://test:test@localhost:5432/crypto_news_test"


def get_config() -> Config:
    """Get appropriate configuration based on environment."""
    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    return DevelopmentConfig()
