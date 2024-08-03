# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        lista = []
        
        while head:
            lista.append(head.val)
            head = head.next
            
        return lista == lista[::-1]
        