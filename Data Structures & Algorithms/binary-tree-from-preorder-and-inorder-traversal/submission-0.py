# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder is root -> l -> r, in-order is l -> root -> r
        first element in preorder is the root. Find the index its at in in-order, then you know everything to the left of it is in l-subtree
        '''
        self.p_ind = 0
        self.preorder = preorder
        self.inorder = inorder
        root = self.recursiveBuild(0, len(self.inorder))

        return root

    def recursiveBuild(self, i_left, i_right):
        if i_left >= i_right:
            return None

        root = TreeNode(self.preorder[self.p_ind])

        i = i_left
        while self.inorder[i] != self.preorder[self.p_ind]:
            i += 1
        
        self.p_ind += 1

        root.left = self.recursiveBuild(i_left, i)
        root.right = self.recursiveBuild(i+1, i_right)

        return root
