# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        h (0)      1          2        3
        n = 1     n=2        n=3      n=None

        Have a prev = None
        curr = head
        Start a while curr is not None loop
        Save curr node's next in a next var
        Set curr node's next to prev
        Set new prev to curr
        set curr to the next var
        
        Time: O(n) - We iterate down the list, switch around the next pointers
        Space: O(1) - We only have prev and curr to account for
        '''

        prev = None
        curr = head
        while curr is not None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        return prev
