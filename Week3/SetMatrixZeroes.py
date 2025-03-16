from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRow, zeroCol = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroRow.add(r)
                    zeroCol.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if ((r in zeroRow) or (c in zeroCol)):
                    matrix[r][c] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution = Solution()
solution.setZeroes(matrix)
print(matrix)