# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        index = 0
        length = len(nums)
        for _ in range(length):
            if nums[index] == 0:
                nums.append(nums.pop(index))
                continue
            index += 1