# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
            


# =========
my_list = list(map(int, input('digits: ').split(' ')))
s = Solution()
print(s.plusOne(my_list))
