class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    diff = n - m

    cur = 1

    while cur <= diff:
      m &= ~cur
      cur <<= 1
    
    return m
