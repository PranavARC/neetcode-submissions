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
        first element in preorder is the root. Find the index it's at in in-order, then you know everything to the left of it is in l-subtree
        Make a dict that maps the pre-order element to its in-order index, create the root with the pre-order element as val
        Then move to the next pre-order element, and give root.left the in-order sublist between the left bound and in-order index
        And give root.right the in-order sublist between in-order index + 1 and the right bound
        Time complexity: O(n) - Creating in-order dict, and going through each element of pre-order
        Space complexity: O(n) - Space for the in-order dict, the recursive stack takes up O(h) 
        '''

        self.p_ind = 0
        self.preorder = preorder
        self.inorder = inorder

        self.inorderDict = dict()

        for i in range(len(inorder)):
            self.inorderDict[inorder[i]] = i

        root = self.recursiveBuild(0, len(self.inorder))

        return root

    def recursiveBuild(self, i_left, i_right):
        if i_left >= i_right:
            return None

        root = TreeNode(self.preorder[self.p_ind])
        
        self.p_ind += 1

        root.left = self.recursiveBuild(i_left, self.inorderDict[root.val])
        root.right = self.recursiveBuild(self.inorderDict[root.val]+1, i_right)

        return root
