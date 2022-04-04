# https://leetcode.com/problems/roman-to-integer/

s = input()
roman_list = list(s.strip())
convert_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

sum = 0

for i in range(0, len(roman_list)):
    value = roman_list[i]
    if i != 0:
        before_value = roman_list[i-1];
        if convert_dict[value] > convert_dict[before_value]:
            sum += (convert_dict[value] - convert_dict[before_value] * 2)
        else:
            sum += convert_dict[value]
    else:
        sum += convert_dict[value]
        pass

print(sum)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_list = list(s.strip())
#         convert_dict = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }

#         sum = 0

#         for i in range(0, len(roman_list)):
#             value = roman_list[i]
#             if i != 0:
#                 before_value = roman_list[i-1];
#                 if convert_dict[value] > convert_dict[before_value]:
#                     sum += (convert_dict[value] - convert_dict[before_value] * 2)
#                 else:
#                     sum += convert_dict[value]
#             else:
#                 sum += convert_dict[value]
        
#         return sum