# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
    
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev 
            prev = current
            current = next_node

        return prev
            
        