import numpy as np

def calculate_retail_price(purchase_price, logistics_rate, it_rate, personnel_rate, profit_margin):
    total_rate = logistics_rate + it_rate + personnel_rate + profit_margin
    retail_price = purchase_price * (1 + total_rate)
    return np.round(retail_price, 2)
