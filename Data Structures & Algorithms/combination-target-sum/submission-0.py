class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        For each number in nums, add it to the list anywhere from 0 to as many times as possible while staying under target
        If target is 0, add that as a valid combo and return, else run the method with the next number in nums
        '''
        self.combos = []
        self.nums = nums
        
        self.recursiveCombos(0, [], target)
        return self.combos
    
    def recursiveCombos(self, curr_ind, curr_list, curr_target):
        if curr_ind == len(self.nums):
            return

        self.recursiveCombos(curr_ind+1, list(curr_list), curr_target)
        
        curr_val = self.nums[curr_ind]
        

        while curr_target >= curr_val:
            curr_list.append(curr_val)
            curr_target -= curr_val

            if curr_target == 0:
                self.combos.append(list(curr_list))
                return
            self.recursiveCombos(curr_ind+1, list(curr_list), curr_target)