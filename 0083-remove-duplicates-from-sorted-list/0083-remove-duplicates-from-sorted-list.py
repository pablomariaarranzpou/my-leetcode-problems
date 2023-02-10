# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = head
        
        if head == None:
            return None
        
        while h.next:
            
            if h.next.val == h.val:
                h.next = h.next.next
            else:
                h = h.next
         
        
        return head