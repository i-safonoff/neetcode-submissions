# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0, root)

        st = [root]

        while st:
            cur = st.pop()
            if not cur:
                continue
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
            
            cur.left, cur.right = cur.right, cur.left
        
        return dummy.left
            
