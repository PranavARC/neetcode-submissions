# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Since we need to fill out a sublist in the height index, we can use a height tracking variable to decide where to insert vals
        Time: O(n) since we traverse each node
        Space: O(n) for the level list
        '''
        level_list = []
        self.recursiveLevels(root, level_list, 0)
        return level_list
    
    def recursiveLevels(self, root, level_list, height):
        if not root:
            return
        
        while len(level_list) < height + 1:
            level_list.append(list())
        
        level_list[height].append(root.val)

        self.recursiveLevels(root.left, level_list, height + 1)
        self.recursiveLevels(root.right, level_list, height + 1)
