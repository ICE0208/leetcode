# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

def swapNodes(head, k):
    head_len = len(head)
    
    temp = head[k]
    head[k] = head[head_len-k+1]
    head[head_len-k+1] = temp

    return head

head = list(map(int, input().split()))
k = int(input())

print(swapNodes(head, k))

# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         list = []
#         n = head
#         while n is not None:
#             list.append(n.val)
#             n = n.next
            
#         head_len = len(list)
#         temp = list[k-1]
#         list[k-1] = list[head_len-k]
#         list[head_len-k] = temp
           
#         result_head = ListNode(list[0])
#         result_tail = result_head
        
#         e = 1
#         while e < len(list):
#             result_tail.next = ListNode(list[e])
#             result_tail = result_tail.next
#             e+=1
    
#         return result_head