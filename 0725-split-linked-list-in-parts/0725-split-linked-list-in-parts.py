# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        ans = [None] * k

        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next

        split_size = size // k
        num_remaining_parts = size % k

        current = head
        for i in range(k):
            new_part = ListNode(0)
            tail = new_part

            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            for j in range(current_size):
                tail.next = ListNode(current.val)
                tail = tail.next
                current = current.next
            ans[i] = new_part.next

        return ans