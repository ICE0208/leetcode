# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i]==target or nums[i]>target:
                return i
        return len_nums
        
# ==============

s = Solution();
nums = list(map(int, input('nums : ').split()))
target = int(input('target : '))

print(s.searchInsert(nums, target))

