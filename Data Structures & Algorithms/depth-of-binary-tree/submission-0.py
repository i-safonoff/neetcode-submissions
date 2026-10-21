# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 1
        st = [(root, 1)]
        while st:
            cur, cur_depth = st.pop()
            if not cur:
                continue
            if cur.left:
                st.append((cur.left, cur_depth + 1))
            if cur.right:
                st.append((cur.right, cur_depth + 1))
            max_depth = max(max_depth, cur_depth)
        return max_depth

            
