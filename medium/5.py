# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s):
        ulti_start_index = 0
        ulti_end_index = 0
        for center_index in range(0, len(s)):
            c_next_index = center_index + 1
            for diff in range(0, len(s)+1):
                if center_index-diff >= 0 and center_index+diff < len(s):
                    if s[center_index-diff] == s[center_index+diff]:
                        continue
                if (center_index+diff-1) - (center_index-diff+1) > ulti_end_index - ulti_start_index:
                    ulti_start_index = center_index-diff+1
                    ulti_end_index = center_index+diff-1
                break

            for diff in range(0, len(s)+1):
                if center_index-diff >= 0 and  c_next_index+diff < len(s):
                    if s[center_index-diff] == s[ c_next_index+diff]:
                        continue
                if (c_next_index+diff-1) - (center_index-diff+1) > ulti_end_index - ulti_start_index:
                    ulti_start_index = center_index-diff+1
                    ulti_end_index =  c_next_index+diff-1
                break



        return s[ulti_start_index:ulti_end_index+1]


        


# =============
s = Solution()
my_str = input('str : ')
print(s.longestPalindrome(my_str))