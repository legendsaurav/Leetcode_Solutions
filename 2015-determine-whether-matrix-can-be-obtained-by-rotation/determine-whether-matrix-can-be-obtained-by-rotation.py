class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            nums=[[0]*len(mat) for i in range(len(mat))]
            for i in range (len(mat)):
                for j in range (len(mat)):
                    nums[j][len(mat)-1-i]=mat[i][j]
            return nums
        for _ in range (4):
            if mat==target:
                return True
            else:
                mat=rotate(mat)
        return False
            
