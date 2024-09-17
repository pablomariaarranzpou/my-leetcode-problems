# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        depth = 1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                node = q.popleft()
                # Since we added nodes without checking null, we need to skip them here.
                if not node:
                    continue
                # The first leaf would be at minimum depth, hence return it.
                if not node.left and not node.right:
                    return depth
                q.append(node.left)
                q.append(node.right)
            depth += 1
        return -1
        
        
        
                
                
        