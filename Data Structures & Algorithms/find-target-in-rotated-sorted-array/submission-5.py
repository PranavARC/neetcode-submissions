class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Given the array is rotated, we can say that the array can be divided into two sorted subarrays
        The point where the first array ends and the second starts is at the lowest value (since that's the rotation point)
        So first, let's go ahead and try to find that lowest value
        
        Take left as 0 and right as the last index of the list (len(nums) - 1) and loop while left is less than right 
        note: We check less than and not LTE since when left == right, both pointers will be at the minimum element
        With mid = l+r//2, compare it to the value of right
        if mid is less than right, this means that everything after mid will be greater, so take right = mid (since mid could be the lowest)
        elif mid is greater than right, this means that the rotation point (aka smallest element) exists between mid and right
        so take left = mid + 1 (since mid can't be the smallest element given that right is smaller)
        Once we exit the loop we will be at the index of the smallest element
        Now perform one binary search with l = 0 and r = left - 1 (since left is the smallest element and start of the 2nd array)
        and the other binary search with l = left and r = len(nums) - 1
        in either case, loop while left <= right (we now check lte since we're trying to search for a value, versus knowing for sure it exists where l=r)
        take mid = l+r//2, if mid == target: return mid, if mid < target: left = mid + 1, and if mid > target: right = mid - 1
        if neither subarray contain the index return -1

        Time: O(logn) - Finding the minimum element is O(logn), searching each subarray will be O(loga) and O(logb) where a+b=n
        Space: O(1) - We don't store anything, and don't create subarrays, just use our knowledge to set l/r bounds between them
        '''

        # Find the minimum element
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]: # everything to the right of mid is greater than mid
                right = mid # mid might still be the smallest element, so include it
            else:   # the rotation point aka minimum element exists between mid and right
                left = mid + 1  # mid can't be the smallest element (since right is smaller), so exclude it

        mini = left
        for left,right in [[0, mini-1], [mini, len(nums)-1]]:
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target: # target is to the right of mid
                    left = mid + 1
                else: # nums[mid] > target, aka target is to the left of mid
                    right = mid - 1
        
        return -1
