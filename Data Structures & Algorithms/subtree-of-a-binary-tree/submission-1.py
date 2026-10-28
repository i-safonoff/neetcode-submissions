# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_same(node, subnode):
            if node is None and subnode is None:
                return True
            elif None in (node, subnode):
                return False
            if node.val != subnode.val:
                return False
            return are_same(node.left, subnode.left) and are_same(node.right, subnode.right)
        
        if root is None:
            return False
        if are_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
