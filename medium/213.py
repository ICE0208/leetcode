# 첫번째 풀이
class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        d = {}
        for i in range(len(nums)-2, -1, -1):
            d[i] = max(d.get(i+2, 0), d.get(i+3, 0)) + nums[i]
        cur_max = max(d.get(0, 0), d.get(1, 0))
        
        for i in range(len(nums)-1, 0, -1):
            d[i] = max(d.get(i+2, 0), d.get(i+3, 0)) + nums[i]
        cur_max2 = max(d.get(1, 0), d.get(2, 0))
        return max(cur_max, cur_max2)