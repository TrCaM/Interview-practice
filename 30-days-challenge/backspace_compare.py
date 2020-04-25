class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    def getNextChar(pos, s):
      countBack = 0
      while countBack >= 0 and pos >= 0:
        if s[pos] == '#':
          countBack += 1
        else:
          countBack -= 1
        pos -= 1
      next_char = s[pos + 1] if countBack < 0 else '#'
      return pos, s[pos + 1]

    pS = len(S) - 1
    pT = len(T) - 1

    while pS >= 0 and pT >= 0:
      pS, charS = getNextChar(pS, S)
      pT, charT = getNextChar(pT, T)
      if charS != charT:
        return false
      
