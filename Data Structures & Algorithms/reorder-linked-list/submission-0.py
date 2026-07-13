# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        From the examples, we can see that the new linked list's order is start -> end -> start + 1 -> end - 1 until we hit the middle
        Brute force: Iterate through all the nodes and assign them to indices in an array, and loop through the indices to set next
        Smart force: Iterate through the list once to find the total number of nodes, and calculate the midpoint
        From the midpoint onwards, set the node's next to the previous node
        So we'd go from: 0->1->2->3->4 to 0->1->2<-3<-4
        Now set left = head, right = tail
        Alternate by setting left's next to right, move left to its og next, then set right's next to left, move right to its og next
        0->4
        Before each alternation, check if left is right, and break if so
        At the end, set left.next to None, since it currently still points to the next element in the original sequence
        Time: O(n) - We iterate through once to find the length, once to reverse the next pointers of the second half, and once to reorder
        Space: O(1) - We just store a couple of pointers
        '''

        curr = head
        length = 0

    
        while curr:
            length += 1
            curr = curr.next
        
        mid = length // 2

        curr = head
        prev = None
        i = 0
        while curr:
            temp = curr.next
            if i > mid:
                curr.next = prev
            prev = curr
            curr = temp
            i += 1

        left = head
        right = prev

        while True:
            if left is right or left is None:
                break
            temp = left.next
            left.next = right
            left = temp
            if right is left or right is None:
                break
            temp = right.next
            right.next = left
            right = temp
        
        if left:
            left.next = None
        
        return
        