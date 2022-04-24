# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        temp_list = []
        k = len(nums)
        n = 0
        while n < k:
            this_num = nums[n]
            if nums[n] in temp_list:
                nums.pop(n)
                k = k-1
            else:
                temp_list.append(this_num)
                n = n+1
        return k

# ======
input_list = list(map(int, input('list : ').split()))
s = Solution()
s.removeDuplicates(input_list)
print(input_list)