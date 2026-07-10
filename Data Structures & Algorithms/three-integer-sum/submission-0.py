class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        zero_triplets = set()
        for i in range(len(nums)):
            curr_num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -curr_num:
                    zero_triplets.add((curr_num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] >= -curr_num:
                    right -= 1
                else:
                    left += 1

        return [list(x) for x in zero_triplets]
