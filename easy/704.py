# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except: # Value Error
            return -1

# =====
s = Solution()
INPUT = [-1, 0, 3, 5, 9, 12]
TARGET = 9
print(s.search(INPUT, TARGET))
                