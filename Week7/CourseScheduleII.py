from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preCrs = defaultdict(list)
        for c, p in prerequisites:
            preCrs[c].append(p)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False

            cycle.add(crs)
            for prev in preCrs[crs]:
                if not dfs(prev):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

def test_findOrder():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    sol = Solution()
    result = sol.findOrder(numCourses, prerequisites)
    print("Course Order:", result)

test_findOrder()
