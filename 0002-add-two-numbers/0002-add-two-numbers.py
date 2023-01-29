# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1, str2 = "", ""

        node = l1
        str1 += str(node.val)

        while node.next != None:
            str1 += str(node.next.val)
            node = node.next


        node = l2
        str2 += str(node.val)

        while node.next != None:
            str2 += str(node.next.val)
            node = node.next

        result = str(int(str2[::-1]) + int(str1[::-1]))

        result_list = [int(x) for x in result[::-1]]
        

        cur = dummy = ListNode(0)
        for e in result_list:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
            

            
