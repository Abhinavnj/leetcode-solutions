def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 0:
        return 0
    
    # minPrice = float('inf')
    minPrice = prices[0]
    maxProfit = 0
    
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
            continue
        maxProfit = max(maxProfit, prices[i] - minPrice)
    
    return maxProfit