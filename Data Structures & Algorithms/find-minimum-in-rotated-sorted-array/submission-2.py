class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        We know that the minimum element of the array will exist where the element to the left is greater than it
        Actually a better way to put it is that it'll exist in the half of the list that is unsorted
        So start with a left and right pointer, loop while left lt(e?) right
        take the mid as l+r//2, and check it against the right
        If the right is larger than mid, it means mid to R is sorted, and everything after mid will be greater, so take right = mid
        not right = mid - 1, since mid could be the lowest possible
        If the right is smaller than mid, it means between mid to R is the rotation point, and thus the minimum, so take left = mid + 1
        not left = mid, since we've already established that right is smaller than mid, so mid can't be the smallest element
        Once we get left == right, both pointers will be on the minimum value (hence why we dont stop looping at LTE), so return left/right
        This is also why we don't compare against left, since in a 2-element array, mid will equal left, though maybe that isn't the biggest deal
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: # everything after nums[mid] will be greater than it
                right = mid # we include mid, since it might be the smallest value
            else: # right being less than something to the left of it means the subarray is unsorted, aka the rotation happened here
                left = mid + 1 # we exclude mid, since we've already found an element smaller than it (aka right)
        
        return nums[left]
