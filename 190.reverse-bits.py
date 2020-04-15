#
# @lc app=leetcode id=190 lang=python3
#
# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
      out = 0
      mask = 0x80000000
      for i in range(16):
        out |= (n & (1 << i)) << (31 -2 *i)
        out |= (n & (mask >> i)) >> (31 -2 *i)
      
      return out
    
    def reverseBits2(self, x):
      x = ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1);
      x = ((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2);
      x = ((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4);
      x = ((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8);
      x = ((x & 0xffff0000) >> 16) | ((x & 0x0000ffff) << 16);
      return x

# @lc code=end