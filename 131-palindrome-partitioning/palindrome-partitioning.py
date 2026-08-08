from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []

        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(start, current):

            if start == len(s):
                ans.append(current.copy())
                return

            for end in range(start, len(s)):

                substring = s[start:end + 1]

                if isPalindrome(substring):
                    current.append(substring)

                    backtrack(end + 1, current)

                    current.pop()

        backtrack(0, [])

        return ans