class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            
            product = 1
            temp = n
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            
            if n == 0:
                product = 0
                
            # Check divisibility
            if product % t == 0:
                return n
            
            n += 1
