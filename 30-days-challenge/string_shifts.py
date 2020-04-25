class Solution:
  def stringShift(self, s: str, shift: List[List[int]]) -> str:
    final_amounts = 0
    for direction, amount in shift:
      final_amounts += amount * (1 if direction else -1)

    length = len(s)
    final_right_shift = final_amounts % length
    out = ["#"] * length
    for i, char in enumerate(s):
      out[(i + final_right_shift) % length] = char

    return "".join(out)
