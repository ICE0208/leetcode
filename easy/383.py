# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_tu = set(ransomNote)
        for i in r_tu:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

# def canConstruct(ransomNote, magazine):
#     r_tu = set(ransomNote)
#     for i in r_tu:
#         if ransomNote.count(i) > magazine.count(i):
#             return False
#     return True

# m = input()
# n = input()

# print(canConstruct(m, n))