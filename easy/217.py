# https://leetcode.com/problems/contains-duplicate/

# O(nlogn) Solution
class Solution:
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        
        temp = nums[0]
        for num in nums[1:]:
            if temp == num:
                return True
            temp = num