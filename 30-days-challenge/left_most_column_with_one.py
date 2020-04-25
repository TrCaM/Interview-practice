# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
  def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    rows, cols = binaryMatrix.dimensions()
    
    first_one_col = -1

    row = 0
    col = cols - 1
    go_left = False
    # Going right until we find 1
    while row < rows and col >= 0:
      if binaryMatrix.get(row, col):
        first_one_col = col
        col -= 1
        go_left = True
      else:
        row += 1
        col += 1 if go_left else 0
        go_left = False


    return first_one_col

      
