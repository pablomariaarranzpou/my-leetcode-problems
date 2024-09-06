# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        nums = set(nums)
        ini = head
        
        while ini.val in nums:
            ini = ini.next
        
        head = ini
        while head.next:
            
            if head.next.val in nums:
                head.next = head.next.next
            else:   
                head = head.next
                
        return ini
        
        