# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/

class Solution:
    def kWeakestRows(self, mat, k):
        soldier_dict = {}
        soldier_count = 0
        for i in range(0, len(mat)):
            soldier_count = mat[i].count(1)
            if soldier_count not in soldier_dict:
                soldier_dict[soldier_count] = list()
            soldier_dict[soldier_count].append(i)

        sorted_sol_list = sorted(soldier_dict.items())

        result_list = list()
        for t in sorted_sol_list:
            for l in t[1]:
                k -= 1
                result_list.append(l)
                if (k < 1):
                    return result_list


# --------------------------------------------------------
# Input Row Count / Input Lists(mat) / Input k
s = Solution()
temp_list = []
n = int(input("n : "))
for i in range(0, n):
    temp_list.append(list(map(int, input().split(" "))))
temp_k = int(input())

print(s.kWeakestRows(temp_list, temp_k))
