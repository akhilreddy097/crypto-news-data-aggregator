"""
Cryptocurrency data aggregator module.

Handles collection and processing of cryptocurrency market data from various sources.
"""

import requests
import pandas as pd
from typing import List, Dict, Any
from datetime import datetime
from loguru import logger


class CryptoAggregator:
    """Aggregates cryptocurrency data from multiple sources."""

    def __init__(self, api_key: str = ""):
        """Initialize the crypto aggregator."""
        self.api_key = api_key
        self.base_url_coingecko = "https://api.coingecko.com/api/v3"
        self.data_buffer = []

    def fetch_crypto_prices(self, crypto_ids: List[str] = None) -> Dict[str, Any]:
        """Fetch current prices for specified cryptocurrencies."""
        if crypto_ids is None:
            crypto_ids = ["bitcoin", "ethereum", "cardano", "solana"]
        
        try:
            params = {
                "ids": ",".join(crypto_ids),
                "vs_currencies": "usd,eur,gbp",
                "include_market_cap": "true",
                "include_24hr_vol": "true",
                "include_24hr_change": "true"
            }
            response = requests.get(
                f"{self.base_url_coingecko}/simple/price",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            logger.info(f"Successfully fetched prices for {len(data)} cryptocurrencies")
            return data
        except requests.RequestException as e:
            logger.error(f"Error fetching crypto prices: {e}")
            return {}

    def fetch_market_data(self) -> Dict[str, Any]:
        """Fetch global cryptocurrency market data."""
        try:
            response = requests.get(
                f"{self.base_url_coingecko}/global",
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            logger.info("Successfully fetched global market data")
            return data
        except requests.RequestException as e:
            logger.error(f"Error fetching market data: {e}")
            return {}

    def process_price_data(self, raw_data: Dict[str, Any]) -> pd.DataFrame:
        """Process raw price data into a pandas DataFrame."""
        records = []
        for crypto, prices in raw_data.items():
            record = {"cryptocurrency": crypto, "timestamp": datetime.now()}
            record.update(prices)
            records.append(record)
        
        df = pd.DataFrame(records)
        logger.info(f"Processed {len(df)} cryptocurrency records")
        return df

    def aggregate_data(self) -> Dict[str, Any]:
        """Aggregate all cryptocurrency data."""
        prices = self.fetch_crypto_prices()
        market_data = self.fetch_market_data()
        
        return {
            "prices": prices,
            "market_data": market_data,
            "timestamp": datetime.now().isoformat()
        }
