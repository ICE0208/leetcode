# https://leetcode.com/problems/add-two-numbers/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = []
        list2 = []
        n = l1
        while n is not None:
            list1.append(n.val)
            n = n.next
        n = l2
        while n is not None:
            list2.append(n.val)
            n = n.next

        len_list1 = len(list1)
        len_list2 = len(list2)
        if len_list1 < len_list2:
            for i in range(len_list2-len_list1):
                list1.append(0)
        else:
            for i in range(len_list1-len_list2):
                list2.append(0)

        print(list1, list2)

        up = 0
        result_list = []
        for i in range(max(len_list1,len_list2)):
            this_sum = list1[i] + list2[i] + up
            result_list.append(this_sum%10)
            up = this_sum//10
        if up!=0:
            result_list.append(up)

        while result_list[-1] == 0 and len(result_list) > 1:
            result_list.pop()

        result_node = ListNode(result_list[0])
        now_node = result_node
        for i in result_list[1:]:
            now_node.next = ListNode(i)
            now_node = now_node.next

        return result_node



# Input List -> Linked List
s = Solution()
temp_list = list(map(int, input('l1 = ').split(" ")))
ln = ListNode(temp_list[0])
now_node = ln
for i in temp_list[1:]:
    now_node.next = ListNode(i)
    now_node = now_node.next
temp_list2 = list(map(int, input('l2 = ').split(" ")))
ln2 = ListNode(temp_list2[0])
now_node2 = ln2
for i in temp_list2[1:]:
    now_node2.next = ListNode(i)
    now_node2 = now_node2.next

# Print Linked List
# n = ln2
# while n is not None:
#     print(n.val)
#     n = n.next
print(s.addTwoNumbers(ln, ln2))


