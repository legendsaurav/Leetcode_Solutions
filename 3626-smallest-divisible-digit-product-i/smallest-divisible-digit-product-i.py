class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate the product of digits
            product = 1
            temp = n
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            # 0 is always divisible by t
            if n == 0:
                product = 0
                
            # Check divisibility
            if product % t == 0:
                return n
            
            n += 1
