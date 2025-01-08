def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        current_profit = prices[i] - min_price
        if current_profit > max_profit:
            max_profit = current_profit
            sell_day = i

    return buy_day + 1, sell_day + 1


prices = [3, 5, 8, 6, 2, 8, 3, 2, 20]
buy_day, sell_day= max_profit(prices)

buy_price = prices[buy_day - 1]
sell_price = prices[sell_day - 1]
fprices = []
fprices.append(buy_price)
fprices.append(sell_price)
print(fprices)