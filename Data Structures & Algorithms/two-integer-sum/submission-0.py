class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in diff_dict:
                return [diff_dict[num], i]
            diff_dict[target-num] = i
        return [-1, -1]
