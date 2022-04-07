# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts):
        money_list = []
        for l in accounts:
            money_list.append(sum(l))

        return max(money_list)
        




# ==========================
s = Solution()
m = int(input('m : '))
l = list()
for i in range(m):
    l.append(list(map(int, input().split(" "))))
print(s.maximumWealth(l))