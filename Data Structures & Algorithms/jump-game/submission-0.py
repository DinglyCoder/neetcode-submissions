class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if (len(nums) == 1):
            return True

        memo = [False] * len(nums)
        memo[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            # print(f"Test {i}")
            for j in range(nums[i]):
                # print(f"{memo[i + j + 1]}")
                if i + j + 1 < len(nums) and memo[i + j + 1]:
                    # print("yo")
                    memo[i] = True
                    break
            
        print(memo)
        return memo[0]
            
        