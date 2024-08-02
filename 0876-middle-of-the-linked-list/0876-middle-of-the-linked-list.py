# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        count = 0
        vals = []
        
        while head:
            
            count += 1
            vals.append(head)
            head = head.next
            
        
  
        return vals[(count)//2]
        