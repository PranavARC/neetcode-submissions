class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = list(pre)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                suf[-(i+1)] = 1
                continue
            elif i == 1:
                pre[i] = nums[i-1]
                suf[-(i+1)] = nums[-i]
                continue
            
            pre[i] = pre[i-1] * nums[i-1]
            suf[-(i+1)] = suf[-i] * nums[-i]

        return [pre[i] * suf[i] for i in range(len(nums))]
