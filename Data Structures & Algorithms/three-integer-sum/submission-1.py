class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums = sorted(nums)
        ret = []

        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1

            while (l < r):
                if (nums[l] + nums[r] < target):
                    l += 1
                elif (nums[l] + nums[r] == target):
                    ans = str(nums[i]) + str(nums[l]) + str(nums[r])
                    if ans not in seen:
                        ret.append([nums[i], nums[l], nums[r]])
                        seen.add(ans)
                    l += 1
                else:
                    r -= 1
        
        return ret
