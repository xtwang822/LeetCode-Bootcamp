from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        sumSet = set()
        sumSet.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for s in sumSet:
                if nums[i] + s == target:
                    return True
                nextDP.add(nums[i] + s)
                nextDP.add(s)
            sumSet = nextDP
        return False

nums = [1, 5, 11, 5]
sol = Solution()
result = sol.canPartition(nums)
print("Can partition:", result)