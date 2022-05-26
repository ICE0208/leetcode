# https://leetcode.com/problems/house-robber/

# 2차 풀이
class Solution:
    def rob(self, nums):
        cash = {}
        
        for i in range(len(nums)-1, -1, -1):
            cash[i] = max(cash.get(i+2, 0), cash.get(i+3, 0)) + nums[i]
        return max(cash.get(0, 0), cash.get(1, 0))

# 1차 풀이
class OldSolution:
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