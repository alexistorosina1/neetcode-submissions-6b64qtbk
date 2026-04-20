class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        L = 0
        num_sum = 0

        for R in range(len(nums)):
            num_sum += nums[R]
            while num_sum >= target:
                length = min(R - L + 1,length)
                num_sum -= nums[L]
                L += 1
        
        return 0 if length == float("inf") else length
