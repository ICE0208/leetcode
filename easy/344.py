# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s):
        s.reverse()


# ! 2 pointer
# def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left, right = left+1, right-1