import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                            and col in range(len(grid[0]))
                            and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


def test_orangesRotting():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    # Expected output: 4
    # Explanation: All fresh oranges rot in 4 minutes.

    sol = Solution()
    result = sol.orangesRotting(grid)
    print("Time to rot all oranges:", result)


test_orangesRotting()
