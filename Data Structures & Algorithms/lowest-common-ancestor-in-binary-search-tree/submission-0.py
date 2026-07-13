# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Intuition would say that you find the lowest common ancestor by DFSing and checking the children for it before checking root
        So create a recursive commonAncestor method that first attempts it on the children, and then if neither of them have it, then on root
        Though how would you know if left beats right? Well since everything in BST is unique, only left or right should have it, so not a concern

        The actual method would search for the two values from root onwards, and if they both exist, return yourself, else return -1

        The biggest inefficiency I can see in this method is that we search for p and q individually, traversing twice when once could be adequate
        '''
        lca = self.recursiveAncestor(root, p, q)

        return lca or root
    
    def recursiveAncestor(self, root, p, q):
        if not root:
            return None
        
        left_ancestor = self.recursiveAncestor(root.left, p, q)
        right_ancestor = self.recursiveAncestor(root.right, p, q)

        if left_ancestor or right_ancestor:
            return left_ancestor or right_ancestor
        
        if self.recursiveSearch(root, p) and self.recursiveSearch(root, q):
            return root
        else:
            return None
    
    def search(self, root, target):
        return self.recursiveSearch(root, target)

    def recursiveSearch(self, root, target):
        if not root:
            return False
        
        if root.val == target.val:
            return True
        
        return self.recursiveSearch(root.left, target) or self.recursiveSearch(root.right, target)
