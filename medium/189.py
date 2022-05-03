# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        temp = nums[-k:]
        nums[-k:] = []
        nums[0:0] = temp
        