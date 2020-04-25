class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    if not preorder:
      return None

    # Working stack stores nodes that we haven't finished their left subtrees
    working_stack = []
    root = TreeNode(preorder[0])
    working_stack.append(root)

    for val in preorder[1:]:
      if val < working_stack[-1].val:
        # If the next val < the value of the top node, we create a new node to its left 
        working_stack[-1].left = TreeNode(val)
        working_stack.append(working_stack[-1].left)
      else:
        # otherwise we pop the stack until the top node's value is less than val
        while len(working_stack) >= 1 and working_stack[-1].val < val:
          parent = working_stack.pop()
        # Add the new node to the top node's right
        parent.right = TreeNode(val)
        # Push the new node to the working_stack
        working_stack.append(parent.right)

    return root

