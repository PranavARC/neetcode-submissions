# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        if l1 None, return l2, elif l2 None return l1
        Now start off with a head pointer = None
        check whether l1 or l2 is smaller, and set head equal to the smaller, and forward that smaller pointer to its next
        set curr = head and begin a loop that breaks if either l1 or l2 are none
        each iteration, compare l1 to l2, set curr.next to the smaller, advance that smaller to its next, then advance curr to its next
        once the loop breaks, check if l1 is None, if so set curr.next to l2, else set to l1
        return head

        Time: O(n) where n is the length of both lists
        Space: O(1) since we account for only two extra nodes, head and curr
        '''
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list2 if list1 is None else list1

        return head
