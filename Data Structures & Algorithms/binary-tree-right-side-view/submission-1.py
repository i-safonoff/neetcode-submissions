# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root, 0)])
        res = [root.val]
        while q:
            node, lvl = q.popleft()
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
            if len(res) < lvl + 1:
                res.append(node.val)
            else:
                res[lvl] = node.val
        return res