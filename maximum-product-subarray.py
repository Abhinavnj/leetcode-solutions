class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep multiplying numbers in array until 0
        # is encountered and the product restarts from there.
        # Both prefix product and suffix product is calculated
        # so that no cases are missed (Ex: [3, -1, 4]).
        reverseNums = nums[::-1]
        for i in range(1, len(nums)):
            # Or returns first object that evaluates to true
            nums[i] *= nums[i - 1] or 1
            reverseNums[i] *= reverseNums[i - 1] or 1
        return max(nums + reverseNums)

        # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple