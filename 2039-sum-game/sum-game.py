class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        left = num[:mid]
        right = num[mid:]

        left_sum = sum(int(x) for x in left if x != '?')
        right_sum = sum(int(x) for x in right if x != '?')

        left_q = left.count('?')
        right_q = right.count('?')

        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)