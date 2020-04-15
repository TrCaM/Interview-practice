#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addLists(l1, l2, mem):
            if not l1 and not l2 and not mem:
                return None
            
            l1 = l1 or ListNode(0)
            l2 = l2 or ListNode(0)
            head = ListNode((l1.val + l2.val + mem) % 10)
            head.next = addLists(l1.next, l2.next, (l1.val + l2.val + mem) // 10)

            return head

        def addLists_iter(l1, l2):
            mem = 0
            dummy = cur = ListNode(0)

            while l1 or l2 or mem:
                l1 = l1 or ListNode(0)
                l2 = l2 or ListNode(0)
                cur.next = ListNode(0)
                mem, cur.next.val = divmod(l1.val + l2.val + mem, 10)
                l1 = l1.next
                l2 = l2.next
                cur = cur.next

            return dummy.next
        
        return addLists_iter(l1, l2)


        
# @lc code=end