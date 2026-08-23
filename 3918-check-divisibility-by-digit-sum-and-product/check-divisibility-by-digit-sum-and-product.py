from math import prod

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        lst = []
        while temp > 0:
            a = temp % 10
            temp = temp // 10
            lst.append(a)
        su_m = sum(lst)
        product = prod(lst)
        return n % (product + su_m) == 0