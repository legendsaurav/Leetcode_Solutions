from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for r in range(1, len(coins) + 1):
                for group in combinations(coins, r):

                    multiple = 1

                    for coin in group:
                        multiple = lcm(multiple, coin)

                    value = x // multiple

                    if r % 2 == 1:
                        total += value
                    else:
                        total -= value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left