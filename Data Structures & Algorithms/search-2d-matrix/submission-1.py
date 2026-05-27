class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # row search

        l = 0
        r = len(matrix) - 1
        mid = -1

        while (l <= r):
            mid = (l + r) // 2

            if (target >= matrix[mid][0] and target <= matrix[mid][-1]):
                break
            elif (target < matrix[mid][0]):
                r = mid - 1
            else:
                l = mid + 1

        if (mid == -1):
            return False

        # col search
        l = 0
        r = len(matrix[0]) - 1

        while (l <= r):
            midCol = (l + r) // 2
            # print(f"{l} and {r} - {midCol}")

            if (target == matrix[mid][midCol]):
                return True
            elif (target < matrix[mid][midCol]):
                r = midCol - 1
            else:
                l = midCol + 1

        return False
        