# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def max_depth(root):
            if root is None:
                return 0
            
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            return 1 + max(left_depth, right_depth)

        return max_depth(root)
