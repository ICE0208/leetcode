# https://leetcode.com/problems/longest-common-prefix/

from asyncio.windows_events import NULL
import keyword


class Solution:
    def longestCommonPrefix(self, strs):
        output_str = str()
        temp_str = str()
        strs.sort(key=lambda x : len(x))
        for i in range(0, len(strs[0])):
            temp_str = strs[0][i]
            for j in range(1, len(strs)):
                if temp_str != strs[j][i]:
                    return output_str
            output_str += temp_str
        return output_str

# =========
s = Solution()
my_str = input('strs : ').split(' ')
print(s.longestCommonPrefix(my_str))