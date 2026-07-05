class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]*-1

        heapq.heapify(nums)

        for i in range(0,k):
            res = heapq.heappop(nums) * -1
            print(res)
            
        return res