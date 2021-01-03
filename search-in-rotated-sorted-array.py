def search(self, nums: List[int], target: int) -> int:
    """
    :nums: List[int]
    :target: int
    :rVal: int
    """

    n = len(nums)
    
    # Find smallest element
    left, right = 0, n - 1
    while (left < right):
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    rotation = left
    
    # Change nums to original order
    nums = (nums + nums[0:rotation])[rotation:]
    
    # Binary search to find target
    left, right = 0, n - 1
    while left <= right: 
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return (mid + rotation) % n
    
    return -1