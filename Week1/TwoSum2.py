from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
    return [l + 1, r + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
