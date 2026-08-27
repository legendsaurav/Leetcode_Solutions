class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the row above the bottom row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Pick the minimum of the two adjacent choices from the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # The top cell now contains the minimum path sum
        return triangle[0][0]