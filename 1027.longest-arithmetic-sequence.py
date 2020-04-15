#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())

    # Not accepted solution
    def longSolution(self, A):
        if len(A) <= 2:
            return len(A)

        longest = 2
        first = 0
        while first < len(A) - longest:
            nxt = first + 1
            while nxt < len(A) - longest:
                step = A[nxt] - A[first]
                seq = 2
                prev = nxt
                cur = nxt + 1
                while cur < len(A):
                    if A[cur] - A[prev] == step:
                        seq += 1
                        prev = cur
                    cur += 1
                longest = max(longest, seq)
                nxt += 1

            first += 1
        return longest


# @lc code=end
