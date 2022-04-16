# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1

        for key, value in my_dict.items():
            if value == 1:
                return key

        # ! 처음 만든 코드
        # ? 런타임이 너무 커서 위에 코드로 수정
        # set_nums = set(nums)
        # for num in set_nums:
        #     if nums.count(num) == 1:
        #         return num

# =========
my_list = list(map(int, input('list : ').split(' ')))
s = Solution()
print(s.singleNumber(my_list))