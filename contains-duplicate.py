def containsDuplicate(nums):
    """
    :nums: List[int]
    :rVal: bool
    """

    # numSet = set()
    # for num in nums:
    #     if num in numSet:
    #         return True
    #     numSet.add(num)
        
    # return False

    return len(set(nums)) != len(nums)