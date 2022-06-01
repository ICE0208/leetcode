# ahttps://leetcode.com/problems/running-sum-of-1d-array/

# 2차 풀이
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# 1차 풀이
class OldSolution:
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