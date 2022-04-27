# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels , stones):
        jewels_list = list(jewels)
        print(jewels_list)
        sum = 0
        for jewel in jewels_list:
            sum += stones.count(jewel)
        return sum

# ==========
# 입력 생략
