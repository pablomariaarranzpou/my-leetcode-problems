# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = head
        while head:
            if head.next:
                head.val, head.next.val = head.next.val, head.val
                head = head.next.next
            else:
                break
        
        return h
    
            
        