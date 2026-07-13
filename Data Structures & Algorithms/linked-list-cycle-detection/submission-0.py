# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Slow and fast pointer. Slow moves once, fast moves twice
        If there is a cycle, slow and fast will end up on the same node before slow reaches the end
        Time: O(n), since only n iterations at most till fast meets slow
        Space: O(1), since we only store slow and fast
        '''
        if not head:
            return False

        slow = head
        fast = head.next

        while slow or fast:
            if slow is fast:
                return True       
            
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
                if fast:
                    fast = fast.next
        
        return False
