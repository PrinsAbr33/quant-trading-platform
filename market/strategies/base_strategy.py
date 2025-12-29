class BaseStrategy:
    def generate_signal(self, data):
        raise NotImplementedError("Strategy must implement generate_signal")
