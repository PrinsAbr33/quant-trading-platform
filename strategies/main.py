from market.market_data import MarketData
from strategies.moving_average import MovingAverageStrategy

data = MarketData("data/sample_data.csv")
market_data = data.load_data()

strategy = MovingAverageStrategy(window=5)
signal = strategy.generate_signal(market_data)

print("Trading Signal:", signal)
