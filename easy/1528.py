# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s, indices):
        length = len(s)
        output = list(range(length))

        for i in range(length):
            output[indices[i]] = s[i]
        return ''.join(output)


# ======
s = Solution()

my_str = "codeleet"
my_indices = [4,5,6,7,0,2,1,3]

print(s.restoreString(my_str, my_indices))