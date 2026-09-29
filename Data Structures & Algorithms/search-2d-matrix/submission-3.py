class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid // n][mid % n] > target:
                r = mid - 1
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                return True

        return False


            