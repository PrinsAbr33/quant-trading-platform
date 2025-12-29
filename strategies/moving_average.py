from strategies.base_strategy import BaseStrategy

class MovingAverageStrategy(BaseStrategy):
    def __init__(self, window=5):
        self.window = window

    def generate_signal(self, data):
        if len(data) < self.window:
            return None

        prices = [row["Close"] for row in data[-self.window:]]
        avg_price = sum(prices) / self.window
        current_price = data[-1]["Close"]

        if current_price > avg_price:
            return "BUY"
        elif current_price < avg_price:
            return "SELL"
        else:
            return "HOLD"
