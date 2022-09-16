# 그리디
from audioop import maxpp


prices=[7,1,5,3,6,4]
def maxProfit(prices):
    result = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result

answer = maxProfit(prices)
print(answer)