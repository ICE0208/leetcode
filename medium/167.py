# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        length = len(numbers)
        already = set()
        for i in range(length-1):
            if numbers[i] in already:
                continue
            already.add(numbers[i])
            
            for j in range(i+1, length):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
            
        