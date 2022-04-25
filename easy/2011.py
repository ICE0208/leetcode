# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for oper in operations:
            x += 1 if oper[1]=='+' else -1
        return x

# ======
opers = input("oper : ").split()
s = Solution()
print(s.finalValueAfterOperations(opers))