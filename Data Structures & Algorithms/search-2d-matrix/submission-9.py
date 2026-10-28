
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l2, r2 = 0, len(matrix)-1
        l, r = 0, len(matrix[0]) - 1

        while l2 <= r2:
            mid = (l2+r2)//2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r2 = mid - 1
            elif matrix[mid][-1] < target:
                l2 = mid + 1
            else:
                l2 = mid
                break

        if l2 > r2:
            return False

        while l <= r:
            mid = (l+r)//2
            if matrix[l2][mid] == target:
                return True
            elif matrix[l2][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
