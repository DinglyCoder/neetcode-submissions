class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [0] * len(nums)

        pre = 1
        post = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(len(output)):
            output[i] = prefix[i] * postfix[i]

        print(prefix)
        print(postfix)

        return output
        

        