def calculate_profit(buy_price, sell_price, quantity):
    profit = (sell_price - buy_price) * quantity
    return round(profit, 2)