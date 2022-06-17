# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1