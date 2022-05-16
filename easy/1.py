# https://leetcode.com/problems/two-sum/

# 두번째 코드
class Solution:
    def twoSum(self, nums , target):
        hashset = set(nums)
        for i in range(len(nums)):
            if target - nums[i] in hashset:
                if i == nums.index(target - nums[i]):
                    continue
                return [i, nums.index(target - nums[i])]
        

# 첫번째 코드
class OldSolution:
    def twoSum(self, nums=[], target=0):
        result = []
        for i in range(len(nums)):
            find_num = target - nums[i]
            if find_num in nums[i+1:]:
                print('find_num:', find_num)
                result.append(i)
                result.append(nums[i+1:].index(find_num)+i+1)
                return result



#  ===========
s = Solution()
l = list(map(int, input("nums : ").split(" ")))
n = int(input('target : '))

print(s.twoSum(l, n))
