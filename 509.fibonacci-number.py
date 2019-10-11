#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
def cache(fib):
    cache = {}

    def decorated_fib(*args):
        if (args in cache):
            return cache[args]
        result = fib(*args)

        cache[args] = result
        return result

    return decorated_fib

class Solution:
    def fib(self, N: int) -> int:
        return self.fib_long(N)

    def fib_recur(self, N: int) -> int:
        """
        Fibonacci with decorator technique
        """
        def fib_cache(N, cache):
            if N <= 1:
                cache[N] = N
                return N

            cache[N] = fib_cache(N-1, cache) + fib_cache(N-2, cache) 

            return cache[N]

        cache = [None] * (N + 1)

        return fib_cache(N, cache)
    
    def fib_dynamic(self, N):
        if N <= 1:
            return N

        start = [0, 1]

        for i in range(2, N + 1):
            start.append(sum(start[-2:]))
        
        return start[-1]
    
    @cache
    def fib_long(self, N):
        if (N < 2):
            return N
        return self.fib_long(N -1) + self.fib_long(N - 2)
    


# @lc code=end

