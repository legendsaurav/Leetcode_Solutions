class Solution:
    def maxProduct(self, n: int) -> int:
        
        lst=[]
        while n>0:
            
            lst.append(n%10)
            n=n//10
        return lst.pop(lst.index(max(lst))) * lst.pop(lst.index(max(lst)))