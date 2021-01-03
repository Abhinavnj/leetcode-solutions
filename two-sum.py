def twoSum(nums, target):
    """
    :nums: List[int]
    :rVal: List[int]
    """

    dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            return [i, dict[complement]]
        dict[nums[i]] = i