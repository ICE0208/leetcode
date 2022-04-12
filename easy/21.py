class Solution:
    def removeElement(self, nums, val):
        result = []
        for num in nums:
            if num != val:
                result.append(num)

        return result


# ==========

nums = list(map(int, input('nums : ').split()))
val = int(input('val : '))
s = Solution()
print(s.removeElement(nums, val))

        