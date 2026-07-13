# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        The simple way about going about this is to test for tree equality at every node,
        and while that's the first thing I shall do, it feels like we might be doing some repeat work, due to possible repeat traversal
        '''
        return self.recursiveSubtree(root, subRoot)

    def recursiveSubtree(self, root, subRoot):
        if self.equalsTree(root, subRoot):
            return True
        
        if not root:
            return False
        
        return self.recursiveSubtree(root.left, subRoot) or self.recursiveSubtree(root.right, subRoot)
    
    def equalsTree(self, root1, root2):
        if not (root1 or root2):
            return True
        elif not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.equalsTree(root1.left, root2.left) and self.equalsTree(root1.right, root2.right)
