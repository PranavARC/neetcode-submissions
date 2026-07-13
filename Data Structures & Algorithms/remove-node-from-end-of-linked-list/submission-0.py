# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        One pass will let us count the length of the list
        The nth node from the end of a list of sz length will be the node at index sz - n
        Use another count variable, and disconnect the nth node from the end and return the head
        (Note, if sz - n = 0, return head.next)
        '''
        if not head:
            return head
        
        length = 0

        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        remove_index = length - n

        if remove_index == 0:
            return head.next
        
        curr = head
        index = 0
        prev = None

        while index < remove_index and curr:
            index += 1
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next if curr else None
        
        return head
