import statistics

def percentchange(old, new):
    return (new-old)*100/old

def volatility(prices):
      returns=[]
      for i in range(1, len(prices)):
          old=prices[i-1]
          new=prices[i]
          returns.append(percentchange(old,new))
      return statistics.stdev(returns)  

if __name__ == "__main__":
    prices1 = [100, 102, 101, 105, 110, 108]
    prices2 = [100, 120, 90, 130, 80, 140]
    print(round(volatility(prices1), 2))
    print(round(volatility(prices2), 2))

