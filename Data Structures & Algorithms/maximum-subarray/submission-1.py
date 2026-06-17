class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10001
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            if nums[i] >= total:
                total = nums[i]

            maxSum = max(maxSum, total)

        return maxSum
            
            
        