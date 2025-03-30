class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        total = 0

        for day in range(1, n + 1):
            if dp[day]:
                for share_day in range(day + delay, min(day + forget, n + 1)):
                    dp[share_day] = (dp[share_day] + dp[day]) % MOD

        for day in range(n - forget + 1, n + 1):
            total = (total + dp[day]) % MOD

        return total

sol = Solution()
print(sol.peopleAwareOfSecret(6, 2, 4))
print(sol.peopleAwareOfSecret(4, 1, 3))
