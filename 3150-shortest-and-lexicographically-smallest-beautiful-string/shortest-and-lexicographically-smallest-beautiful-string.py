class Solution:

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        minimum = float("inf")

        lst = []
        answer = []

        for i in range(len(s)):
            if s[i] == "1":
                lst.append(i)

        if len(lst) < k:
            return ""

        bst = lst[:k]

        def max_current(bst):
            nonlocal minimum, answer

            current = bst[-1] - bst[0]
            sub = s[bst[0]:bst[-1] + 1]

            if current < minimum or (current == minimum and sub < s[answer[0]:answer[-1] + 1]):
                minimum = current
                answer = bst[:]

            return bst

        max_current(bst)

        for i in range(k, len(lst)):
            bst = bst[1:] + [lst[i]]
            max_current(bst)

        return s[answer[0]:answer[-1] + 1]