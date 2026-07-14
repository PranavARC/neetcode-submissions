# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Given that the tree is a BST with unique nodes, we can rely on the following property:
        values in the left subtree are lower, values in the right subtree are higher
        We also know that both p and q WILL exist in the subtree
        So we can just progress through the tree, check the root and its kids values
        We try and see if p and q can exist in one of the roots subtrees (aka if p and q < root or root < p and q)
        If so, we run the same check on that subtree root, else we return the tree
        Note: Make sure you check if root is p/q, otherwise, we'll end up progressing down its child
        Time: O(h) - We only perform as many iterations as the max height of the tree, since we move down after each iteration
        Space: O(h) - We will have h recursions
        '''
        return self.recursiveAncestor(root, p, q)
    
    def recursiveAncestor(self, root, p, q):
        if not root:
            return root

        if root.left and p.val < root.val and q.val < root.val:
                return self.recursiveAncestor(root.left, p, q)

        if root.right and root.val < p.val and root.val < q.val:
                return self.recursiveAncestor(root.right, p, q)
        
        return root
