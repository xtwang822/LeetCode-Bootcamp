from collections import Counter
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    pMap = Counter(p)
    sMap = Counter(s[:len(p) - 1])
    res = []
    l = len(p)

    for i in range(len(p) - 1, len(s)):
        sMap[s[i]] += 1

        if sMap == pMap:
            res.append(i - l + 1)

        sMap[s[i - l + 1]] -= 1
        if sMap[s[i - l + 1]] == 0:
            del sMap[s[i - l + 1]]

    return res

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))