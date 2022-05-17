# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        if nums.count(0) == 1:
            prd = 1
            rst = [0] * len(nums)
            for n in nums:
                if n==0: continue
                prd *= n
            rst[nums.index(0)] = prd
            return rst
        
        prd = 1
        for n in nums:
            prd *= n
        rst = [prd] * len(nums)
        for i in range(len(nums)):
            nums[i] = prd // nums[i]
            
        return nums