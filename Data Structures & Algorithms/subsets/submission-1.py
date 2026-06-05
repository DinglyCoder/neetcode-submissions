class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []

        self.backtracking(nums, 0, [])

        return self.subsets

    def backtracking(self, nums, index, curSet):
        if (index == len(nums)):
            deepCopy = []
            for i in curSet:
                deepCopy.append(i)
            self.subsets.append(deepCopy)
            return
        
        curSet.append(nums[index])
        self.backtracking(nums, index + 1, curSet)
        curSet.pop()
        self.backtracking(nums, index + 1, curSet)

    
        