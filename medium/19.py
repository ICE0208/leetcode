# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        my_list = []
        cur = head
        while cur != None:
            my_list.append(cur.val)
            cur = cur.next
        print(my_list)
        my_list.pop(-n)

        if len(my_list) > 0:
            result = ListNode()
            result.val = my_list[0]
            cur = result

            for i in my_list[1:]:
                cur.next = ListNode()
                cur = cur.next
                cur.val = i

            return result

        else:
            return None

        