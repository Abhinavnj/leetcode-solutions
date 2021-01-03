def findMin(nums):
    """
    :nums: List[int]
    :rVal: int
    """

    # If array is not rotated
    if nums[-1] >= nums[0]:
        return nums[0]
    
    # The inflection point is the point where the array changes
    # from each consecutive element being less than the one before
    # to the next element being less. Everything to the left of the 
    # inflection point is less than it and everything to the right 
    # of the inflection point is greater than it. So, binary search 
    # needs to find this inflection point, which is also the minimum.
    left, right = 0, len(nums) - 1
    while (left < right):
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]