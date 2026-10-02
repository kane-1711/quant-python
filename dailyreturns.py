import statistics
prices2 = [100, 120, 90, 130, 80, 140]
returns = []
def percentchange(old, new):
    return (new - old) * 100 / old
for i in range(1, len(prices2)):
    old = prices2[i - 1]
    new = prices2[i]
    change = percentchange(old, new)
    returns.append(change)
    print("Change in price on day", i + 1, ":", round(change, 2))
print("Average return =", round(sum(returns) / len(returns), 2))
print("Maximum return =", round(max(returns), 2))
print("Minimum return =", round(min(returns), 2))
print("Best day = Day", returns.index(max(returns)) + 2)
print("Volatility =", round(statistics.stdev(returns), 2))