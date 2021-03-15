def maxProfit(prices):
    """
    prices: List[int]
    rVal: int
    """
    if len(prices) == 0:
        return 0
    
    # minPrice = float('inf')
    minPrice = prices[0]
    maxProfit = 0
    
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            # Does not change the maxProfit immediately.
            # Finds mins to compare the next values with.
            minPrice = prices[i]
            continue

        # Check differences starting from the current min until the next min
        # is encountered.
        # Values to the right of the leftmost min keep being checked
        # and the min is reset when another min is found and the rest of
        # the values are compared.
        # Only changes maxProfit once a greater profit is found.
        maxProfit = max(maxProfit, prices[i] - minPrice)
    
    return maxProfit