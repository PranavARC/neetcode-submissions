# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        At each root, there are two categories of maxPaths that can be returned:
        Extendable: Paths that can be have the parent of the current node connected to it (will always include the root of the child) -
        The root itself, the root plus its left subtree's max extendable path, the root plus its right subtrees max extendable path
        Non-extendable: Paths that can't - The root plus the left subtree's extendable path plus the right subtree's extendable path
        The extendable and non-extendable paths of the left and right subtrees (extendable path becomes unextendable if you don't include root)

        The final expression at the original root can just take the max of either of the extendable and non-extendable paths

        NOTE: Remember that if a path forks at the root (aka includes left and right, it cannot be extended, since it'd be a split)

        Time - O(n) - Each node's value is considered once, and the max will always be done between 6 values for each node
        Space - O(h) - Only h number of functions will be active at a time on the recursive stack
        '''
        
        maxPaths = self.recursiveMaxPath(root)
        print(maxPaths)

        return int(max(list(maxPaths.values())))
    
    def recursiveMaxPath(self, root):
        if not root:
            return {"extend": -float('inf'), "nonExtend": -float('inf')}

        maxPathLeft = self.recursiveMaxPath(root.left)
        maxPathRight = self.recursiveMaxPath(root.right)

        extendMaxPaths = [root.val, maxPathLeft["extend"]+root.val, maxPathRight["extend"]+root.val]
        nonExtendMaxPaths = [maxPathLeft["extend"], maxPathRight["extend"], maxPathLeft["nonExtend"], maxPathRight["nonExtend"], maxPathLeft["extend"]+root.val+maxPathRight["extend"]]

        maxExtend = max(extendMaxPaths)
        maxNonExtend = max(nonExtendMaxPaths)

        return {"extend": maxExtend, "nonExtend": maxNonExtend}
