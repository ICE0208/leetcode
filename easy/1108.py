# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

# ========
my_address = input('address = ')
s = Solution()
print(s.defangIPaddr(my_address))