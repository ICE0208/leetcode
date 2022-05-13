# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums)
        
        b = nums[-2]
        c = nums[-1]
        a = nums[-3] + c

        for i in range(len(nums)-4, -1, -1):
            temp = a
            a = max(b, c) + nums[i]
            c = b
            b = temp
            
        return max(a, b)