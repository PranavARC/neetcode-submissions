# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Instead of trying to merge every list together at once, it should be easier to merge 2 at a time, and then merge each next one
        1. def mergeLists:
        Check if either list is empty and return either list if so
        Check which list has the smallest head, set that as our merged head, and advance the smaller list
        Create a loop while the two lists aren't None that compares the heads, sets curr node's next to that, advances curr,
        and advances that list, and once the loop breaks, set the curr's next to the non-None list, and returns the list
        '''

        if len(lists) == 0:
            return None
        
        final_list = lists[0]

        for i in range(1, len(lists)):
            new_list = lists[i]
            final_list = self.mergeLists(final_list, new_list)
            
        return final_list
    
    def mergeLists(self, final_list, new_list):
        if not final_list or not new_list:
            return new_list or final_list

        head = None
        if final_list.val < new_list.val:
            head = final_list
            final_list = final_list.next
        else:
            head = new_list
            new_list = new_list.next
        
        curr = head
        while final_list and new_list:
            if final_list.val < new_list.val:
                curr.next = final_list
                final_list = final_list.next
            else:
                curr.next = new_list
                new_list = new_list.next
            curr = curr.next
        
        curr.next = new_list or final_list
        return head