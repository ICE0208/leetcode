# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph):
        length = len(graph)

        i_dict = dict()
        for i in range(length):
            i_dict[i] = -1

        graph_dict = dict()
        for i in range(length):
            graph_dict[i] = graph[i]

        no_check_list = list(range(length))
        for u in range(0, length):
            if u not in no_check_list:
                continue
            no_check_list.remove(u)
            stack = graph[u]
            substack = []
            while stack or substack:
                if not stack:
                    temp = substack.pop()
                    u = temp
                    stack = graph[temp]
                v = stack.pop()
                if v in no_check_list:
                    substack.append(v)
                    no_check_list.remove(v)
                
                i_dict_u = i_dict[u]
                i_dict_v = i_dict[v]
                if i_dict_u == -1:
                    if i_dict_v == -1: # 아무것도 할당안됨
                        i_dict[u] = 0
                        i_dict[v] = 1
                    
                    else: # v만 할당 됨
                        i_dict[u] = (i_dict_v+1)%2

                else:
                    if i_dict_v == -1: # u만 할당 됨
                        i_dict[v] = (i_dict_u+1)%2

                    else:  # u와 v가  할당 됨
                        if i_dict_u == i_dict_v:
                            return False

        return True

# =========

s = Solution()
GRAPH = [[1,2,3],[0,2],[0,1,3],[0,2]]

print(s.isBipartite(GRAPH))