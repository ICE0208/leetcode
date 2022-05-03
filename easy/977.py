# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        nums = sorted(nums, key= lambda x : abs(x))
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return nums

# ======
s = Solution()
INPUT = [-4,-1,0,3,10]
print(s.sortedSquares(INPUT))
        