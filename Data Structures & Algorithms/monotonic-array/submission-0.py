class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc += 1
                dec += 1

        if inc == len(nums) or dec == len(nums):
            return True
        return False
        