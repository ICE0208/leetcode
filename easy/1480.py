# ahttps://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        sum_ary = []
        sum = 0
        for value in nums:
            sum += value
            sum_ary.append(sum)
        return sum_ary
# ========

s = Solution()
my_nums = list(map(int, input('nums = ').split(' ')))

print(s.runningSum(my_nums))