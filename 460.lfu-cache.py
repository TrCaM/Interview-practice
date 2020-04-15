#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict

class ListNode:
    def __init__(self, value):
        self.val = value
        self.freq = 0
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.sentinal = ListNode(0)
        self.sentinal.next = self.sentinal
        self.sentinal.prev = self.sentinal
    
    def remove(self, node):
        """
        Assume that this node always exists in the list
        """
        n, p = node.next, node.prev
        n.prev, p.next = p, n
        self.head = sentinal.next
        self.tail = sentinal.prev
    
    def tail(self):
        return self.sentinal.prev
    
    def head(self):
        return self.sentinal.next
    
    def addBefore(self, node, next):
        node.next = next
        node.prev = next.prev
        node.prev.next = node
        node.next.prev = node

    def addAfter(self, node, prev):
        node.prev = prev
        node.next = prev.next
        node.prev.next = node
        node.next.prev = node

class FrequencyList:
    def __init__(self):


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.fill = 0
        self.frequenciesList = { 'frequencies': {}, 'queue': DoubleLinkedList()}
        self.nodes = { 'keys': {}, 'queue': DoubleLinkedList()}

    def get(self, key: int) -> int:
        pass


    def put(self, key: int, value: int) -> None:
        if key in self.nodes['keys']:
            node = self.nodes['keys'][key]
            # Work on old freqList
            oldFreqList = self.frequenciesList['frequencies'][node.freq] # This is dblLinkedList
            oldFreqList.remove(node)
            node.freq += 1
            node.val = value




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

