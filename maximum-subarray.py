def maxSubArray(nums):
    """
    :nums: List[int]
    :rVal: int
    """

    # Kadane's Algorithm
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            
    return max(nums)