class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    if not head:
      return head
    slow = fast = head
    while fast.next and fast.next.next:
      fast = fast.next.next
      slow = slow.next
    return slow.next if fast.next else slow


