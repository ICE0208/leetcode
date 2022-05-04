# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position):
        min_cost = float("inf")
        
        for pos in position:
            cur_cost = 0
            isOdd = pos%2
            for v in position:
                if v%2 == isOdd:
                    continue
                cur_cost += 1
            min_cost = min(min_cost, cur_cost)
        return min_cost
                    