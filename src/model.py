import pandas as pd
from .price_calculator import calculate_retail_price

def generate_price_table(df, logistics_rate, it_rate, personnel_rate, profit_margin):
    df["Retail Price"] = df["purchase_price"].apply(
        lambda x: calculate_retail_price(x, logistics_rate, it_rate, personnel_rate, profit_margin)
    )
    return df
