# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s):
        # ? New Code (2022-05-07)
        char_count = len(set(s))
        len_s = len(s)
        for i in range(char_count, -1, -1):
            for j in range(0, len_s - i + 1):
                if len(set(s[j:j+i])) == i:
                    return i

        # ? Old Code (2022-04-07)
        # s_list = list(s)
        # temp_list = []
        # cnt = 0
        # max_cnt = 0
        # for i in range(len(s_list)):
        #     for c in s_list[i:]:
        #         if c not in temp_list:
        #             temp_list.append(c)
        #             cnt += 1
        #         else:
        #             max_cnt = max(max_cnt, cnt)
        #             cnt = 0
        #             temp_list = []
        #             break

        #     max_cnt = max(max_cnt, cnt)

        # return max_cnt

# =============
s = Solution()
string = input("s = ")
print(s.lengthOfLongestSubstring(string))