class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 1. Compute total prefix sum
        pref_sum = sum(stones)
        
        # 2. Base case: taking all stones leaves 0 remaining score for the next player
        ans = pref_sum
        
        # 3. Iterate backwards from the second to last index down to index 1 (x > 1)
        for i in range(len(stones) - 2, 0, -1):
            pref_sum -= stones[i + 1]
            ans = max(ans, pref_sum - ans)
            
        return ans