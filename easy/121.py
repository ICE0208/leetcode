# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        
        l, r = 0, 1
        max_profit = 0
        ct = 0
        while l < len(prices)-1:
            if prices[l] > prices[r]:
                l+=1
                r+=1
                continue
            
            while r < len(prices):
                if prices[l] > prices[r]:
                    l=r
                    r=l+1
                    ct = 1
                    break
                
                max_profit = max(max_profit, prices[r] - prices[l])
                r+=1
            if not ct:
                break
            ct = 0
        return max_profit
                