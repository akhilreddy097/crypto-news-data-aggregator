# Crypto-News Data Aggregator

🚀 A comprehensive real-time data aggregator that pulls cryptocurrency market data and news articles from multiple sources. Designed for traders, analysts, and developers who need unified access to crypto market information.

## Features

✨ **Core Features:**
- 📊 Real-time cryptocurrency price aggregation from CoinGecko API
- 📰 News scraping from multiple sources (NewsAPI, RSS feeds, blockchain media)
- 💾 Multi-database support (PostgreSQL, MongoDB)
- 📈 Market data analysis and processing with Pandas
- 🎨 Data visualization dashboards with Plotly and Matplotlib
- ⚙️ Configurable data collection intervals and sources
- 🔄 Automatic retry logic with exponential backoff
- 📝 Comprehensive logging with loguru
- 🧪 Unit tests and integration tests
- 🐳 Docker support (coming soon)

## Tech Stack

- **Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **APIs:** CCXT, CoinGecko, NewsAPI
- **Database:** PostgreSQL, MongoDB
- **Web Framework:** Flask
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Testing:** Pytest
- **Code Quality:** Black, Flake8, Pylint

## Project Structure

```
crypto-news-data-aggregator/
├── main.py                 # Application entry point
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
├── LICENSE               # MIT License
├── src/
│   ├── __init__.py
│   ├── crypto_aggregator.py    # Cryptocurrency data collection
│   ├── news_aggregator.py      # News data scraping
│   ├── database.py             # Database operations
│   ├── data_processor.py       # Data processing pipeline
│   └── visualizer.py           # Data visualization
├── tests/
│   ├── test_crypto_aggregator.py
│   ├── test_news_aggregator.py
│   └── test_database.py
├── logs/                 # Application logs
└── data/                 # Output data storage
```

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12+ (optional, for SQL database)
- MongoDB 4.0+ (optional, for NoSQL database)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/akhilreddy097/crypto-news-data-aggregator.git
cd crypto-news-data-aggregator
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your API keys and database URLs
```

## Configuration

Create a `.env` file in the project root:

```env
# Cryptocurrency APIs
COINGECKO_API_KEY=your_key
CCXT_EXCHANGE=binance
CCXT_API_KEY=your_key
CCXT_SECRET=your_secret

# News APIs
NEWS_API_KEY=your_key

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/crypto_news_db
DB_TYPE=postgresql

# Server
FLASK_ENV=development
SERVER_PORT=5000
```

## Usage

### Run the aggregator:
```bash
python main.py
```

### Fetch cryptocurrency data:
```python
from src.crypto_aggregator import CryptoAggregator

agg = CryptoAggregator(api_key="your_key")
prices = agg.fetch_crypto_prices(["bitcoin", "ethereum"])
market_data = agg.fetch_market_data()
```

### Fetch news:
```python
from src.news_aggregator import NewsAggregator

news_agg = NewsAggregator(api_key="your_key")
articles = news_agg.fetch_crypto_news()
```

## API Documentation

See [API.md](docs/API.md) for detailed API documentation.

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_crypto_aggregator.py
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Add Telegram/Discord bot integration
- [ ] Implement machine learning for price prediction
- [ ] Add real-time alerts based on price movements
- [ ] Docker containerization
- [ ] REST API with FastAPI
- [ ] WebSocket support for real-time updates
- [ ] Advanced data visualization dashboards
- [ ] Support for additional exchanges (Kraken, Coinbase, etc.)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Support

For issues and questions, please open an issue on GitHub.

## Author

**Akhil Reddy** - [GitHub Profile](https://github.com/akhilreddy097)

---

⭐ If you find this project helpful, please consider giving it a star!
