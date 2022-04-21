# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        list_a = list(map(int, a.strip()))
        list_b = list(map(int, b.strip()))
        result = ""
        temp = 0
        carry = 0
        for _ in range(min(len(list_a), len(list_b))):
            temp = list_a.pop(-1) + list_b.pop(-1)
            result = str((temp+carry)%2) + result
            carry = (temp+carry)//2

        if (len(list_a) > 0):
            longer_list = list_a
        else:
            longer_list = list_b

        for _ in range(len(longer_list)):
            temp = longer_list.pop(-1)
            result = str((temp+carry)%2) + result
            carry = (temp+carry)//2
        if carry > 0:
            result = '1' + result
        return result

# =======
s = Solution()
a, b = input('input : ').split(' ')
print(s.addBinary(a, b))