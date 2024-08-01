# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()
        
        if not head:
            return False
        
        act = head

        
        while act:
            if act in visited:
                return True
            visited.add(act)
            act = act.next
                
            
        return False