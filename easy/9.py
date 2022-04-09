# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        list_x = list(str(x))
        for _ in range(0, len(list_x)//2):
            if list_x.pop(0) != list_x.pop(-1):
                return False
        return True


# ===================
s = Solution()

input_x = int(input('x : '))
print(s.isPalindrome(input_x))
