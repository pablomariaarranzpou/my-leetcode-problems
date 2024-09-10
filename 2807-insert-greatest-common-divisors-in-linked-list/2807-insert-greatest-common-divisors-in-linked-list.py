# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = head
        
        second = head.next
        
        
        while first and second:
            first.next = ListNode(gcd(first.val, second.val), second)
            
            first = second
            
            second = first.next
            
            
        return head
        
        
        
        