# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command):
        result = []
        i = 0
        while i < len(command):
            this_c = command[i]
            if this_c == '(':
                if command[i+1] == ')':
                    result.append('o')
                    i+=2
                    continue
                else:
                    i+=1
                    continue
            elif this_c == ')':
                i+=1
                continue
            else:
                result.append(this_c)
                i+=1
                continue
        return "".join(result)
                


# ======
s = Solution()
print(s.interpret('G()(al)'))
print(s.interpret('G()()()()(al)'))
print(s.interpret('(al)G(al)()()G'))