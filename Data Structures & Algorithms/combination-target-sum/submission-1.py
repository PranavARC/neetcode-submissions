class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        For each number we have two choices:
        1. Add number to the list, subtract it from target, 
        and repeat the process with the same number but with new list/target
        2. Move to the next number with the original list/target

        At any point in this process, if target ends up as 0, we want to add that as a valid combo.
        But if we reach the end of list or the target is below 0, we end as it's a failed branch.

        Time: O(2^(T/M)) - We get 2 choices each time, and T/M for smallest number M is since that number can be taken T/M times
        Space: O(T/M) - Only T/M calls can be made per branch before we backtrack
        '''
        self.combos = []
        self.nums = nums
        
        self.recursiveCombos(0, [], target)
        return self.combos
    
    def recursiveCombos(self, curr_ind, curr_list, curr_target):
        if curr_target == 0:
            self.combos.append(curr_list)
            return
        elif curr_ind == len(self.nums) or curr_target < 0:
            return

        self.recursiveCombos(curr_ind+1, list(curr_list), curr_target)

        curr_val = self.nums[curr_ind]
        curr_list.append(curr_val)
        curr_target -= curr_val
        self.recursiveCombos(curr_ind, list(curr_list), curr_target)
