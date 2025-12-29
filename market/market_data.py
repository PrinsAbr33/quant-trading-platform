import csv
from datetime import datetime

class MarketData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["Date"] = datetime.strptime(row["Date"], "%Y-%m-%d")
                row["Close"] = float(row["Close"])
                self.data.append(row)

        return self.data
