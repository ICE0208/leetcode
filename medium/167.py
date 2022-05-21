# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# ? 2022-05-21 재풀이
class Solution_2:
    def twoSum(self, numbers, target):
        num_set = set(numbers)
        for n in numbers:
            if target-n in num_set:
                if n==target-n and numbers.count(n)==1:
                    continue
                
                n_index = numbers.index(n)
                return [n_index+1, numbers.index(target-n, n_index+1)+1]
        return None

class Solution_1:
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
            
        