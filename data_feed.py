from backtrader.feeds import PandasData
import pandas as pd
import backtrader as bt
from datetime import datetime


class MyDataFeed(bt.feeds.PandasData):
    params = (
        ("fromdate", datetime(2015, 1, 1)),
        ("todate", datetime(2021, 3, 31)),
        ("nullvalue", 0.0),
        ("dtformat", "%Y-%m-%d %H:%M:%S"),
        ("datetime", 0),
        ("open", 1),
        ("high", 2),
        ("low", 3),
        ("close", 4),
        ("volume", 5),
        ("openinterest", -1),
    )

    def __init__(self):
        df = pd.read_csv(
            "bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv",
            skiprows=1,
            header=None,
            names=[
                "Timestamp",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume_(BTC)",
                "Volume_(Currency)",
                "Weighted_Price",
            ],
        )

        # Remove NaN values
        df.dropna(inplace=True)

        # Convert the Timestamp column to datetime and set it as the index
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s")
        df.set_index("Timestamp", inplace=True)

        super().__init__(dataframe=df, **self.params)
