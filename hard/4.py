# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        all_nums = nums1 + nums2
        all_nums.sort()
        len_all_nums = len(all_nums)//2
        return (all_nums[len_all_nums] + all_nums[-(len_all_nums+1)]) / 2


# =====================
list1 = list(map(int, input('list1 = ').split(" ")))
list2 = list(map(int, input('list2 = ').split(" ")))

s = Solution()

print(s.findMedianSortedArrays(list1, list2))