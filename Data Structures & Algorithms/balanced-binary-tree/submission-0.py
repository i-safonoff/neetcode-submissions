# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(head):
            if not head:
                return 0, True
            
            l, is_l = is_balanced(head.left)
            r, is_r = is_balanced(head.right)

            if not (is_l and is_r):
                return 0, False
            
            if abs(l - r) <= 1:
                return max(l, r) + 1, True
            
            return 0, False
        
        _, res = is_balanced(root)

        return res