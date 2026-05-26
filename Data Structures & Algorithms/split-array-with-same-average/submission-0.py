class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)

        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n - 1, 0, -1):
                for s in list(dp[k - 1]):
                    dp[k].add(s + num)

        for k in range(1, n):
            if (k * total) % n == 0:
                target = (k * total) // n

                if target in dp[k]:
                    return True

        return False