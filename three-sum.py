class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # Run 2Sum on each element's complement
            dict = {}
            target = 0 - nums[i]
            for j in range(len(nums)):
                if i != j:
                    complement = target - nums[j]
                    if complement in dict:
                        newList = sorted([nums[j], complement, nums[i]])
                        if newList not in result:
                            result.append(newList)
                    dict[nums[j]] = j
                    
        return result