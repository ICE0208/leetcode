class Solution:
    def missingNumber(self, nums):
        hashset = set()
        max_num = 0
        for n in nums:
            hashset.add(n)
            max_num = max(max_num, n)
        tempset = set(range(0, max_num+1))
        missing_number = tempset - hashset
        if missing_number:
            return missing_number.pop()
        else:
            return max_num + 1