# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        open_list = ['(', '{', '[']
        close_dict = {')':'(', '}':'{', ']':'['}
        temp_open_list = []
        len_s = len(s)
        if len_s%2 == 1:
            return False
        else:
            list_s = list(s)
            for i in range(len_s):
                this_s = list_s.pop(0)
                # when open char
                if this_s in open_list:
                    temp_open_list.append(this_s)
                # when close char
                else:
                    if len(temp_open_list)==0 or close_dict[this_s] != temp_open_list.pop(-1):
                        return False
            
            if len(temp_open_list) > 0:
                return False

            return True

# =======
s = Solution()
my_str = input('str : ')
print(s.isValid(my_str))