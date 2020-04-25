class Solution:
  def checkValidString(self, s: str) -> bool:
    open_brackets = 0      
    stars = 0

    for c in s:
      if c == '*':
        stars += 1
      elif c == '(':
        open_brackets += 1
      else:
        if open_brackets > 0:
          open_brackets -= 1
        elif stars > 0:
          stars -= 1
        else:
          return False

    return open_brackets <= stars



