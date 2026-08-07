class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs (curr,open_count,close_count):
            if len(curr)==2*n:
                ans.append(curr)
                return
            if open_count<n:
                dfs(curr+"(",open_count+1,close_count)
            if close_count<open_count:
                dfs(curr+")",open_count,close_count+1)
        dfs("",0,0)
        return ans