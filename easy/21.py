# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


# ==========

nums = list(map(int, input('nums : ').split()))
val = int(input('val : '))
s = Solution()
print(s.removeElement(nums, val))

        