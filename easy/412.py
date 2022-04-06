# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int):
        fizz_string = "Fizz"
        buzz_string = "Buzz"
        answer = []
        for i in range(1,n+1):
            if (i%3 == 0 or i%5 == 0):
                if (i%3 == 0 and i%5 == 0):
                    answer.append(fizz_string+buzz_string)
                elif (i%3 == 0):
                    answer.append(fizz_string)
                else:
                    answer.append(buzz_string)
            else:
                answer.append(str(i))
        return answer


# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
solution = Solution()
num = int(input())
print(solution.fizzBuzz(num))