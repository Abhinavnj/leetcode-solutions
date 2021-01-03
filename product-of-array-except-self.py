def productExceptSelf(nums):
    """
    :nums: List[int]
    :rVal: List[int]
    """

    numsLen = len(nums)
    output = [1]
    
    for i in range(numsLen - 1):
        output.append(output[-1] * nums[i])
        
    rightProd = 1
    for i in reversed(range(numsLen)):
        output[i] *= rightProd
        rightProd *= nums[i]
    
    return output
    
    # numsLen = len(nums)
    
    # left = [nums[0]] * numsLen
    # right = [nums[-1]] * numsLen
    
    # i = 1
    # j = numsLen - 2
    # while i < numsLen:
    #     left[i] = nums[i] * left[i - 1]
    #     right[j] = nums[j] * right[j + 1]
    #     i += 1
    #     j -= 1
    
    # left.insert(0, 1)
    # right.append(1)
    # left.pop()
    # right.pop(0)
    
    # output = [0] * numsLen
    # for i in range(numsLen):
    #     output[i] = left[i] * right[i]
        
    # print("left:", left)
    # print("right:", right)
    
    # return output