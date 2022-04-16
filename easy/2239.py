# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums):
        c_to_zero = nums.pop(0) # because of n >= 1
        for num in nums:
            if abs(num) < abs(c_to_zero):
                c_to_zero = num
            elif abs(num) == abs(c_to_zero):
                c_to_zero = max(num, c_to_zero)
        return c_to_zero

# =======
my_nums = list(map(int, input('nums: ').split(' ')))
s = Solution()

print(s.findClosestNumber(my_nums))