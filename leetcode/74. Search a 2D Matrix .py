from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = []
        for list in matrix:
            if target >= list[0] and target <= list[len(list) - 1]:
                x = list
                break
        # binary search
        low = 0
        high = len(x) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if x[mid] < target:
                low = mid + 1
            elif x[mid] > target:
                high = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    matrix = [[1]]
    target = 0
    s = Solution()
    print(s.searchMatrix(matrix, target))