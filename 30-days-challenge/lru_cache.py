class Node:
  def __init__(self, val):
    self.val = val 
    self.next = None
    self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.sentinal = Node(0)
      self.sentinal.next = self.sentinal
      self.sentinal.prev = self.sentinal
      self.elements = 0
      self.map = dict()

    def remove(self, node):
      node.prev.next = node.next
      node.next.prev = node.prev

    def add_to_tail(self, node):
      # Add visited element to tail
      tail = self.sentinal.prev
      tail.next = node
      node.prev = tail
      node.next = self.sentinal
      self.sentinal.prev = node

    def remove_head(self):
      head = self.sentinal.next
      self.sentinal.next = head.next
      head.next.prev = self.sentinal
      return head
        
    def get(self, key: int) -> int:
      if key in self.map:
        val, node = self.map[key]
        self.remove(node)
        self.add_to_tail(node)
        return val
      return -1

    def put(self, key: int, value: int) -> None:
      if key in self.map:
        val, node = self.map[key]
        self.remove(node)
      elif self.elements < self.capacity:
        node = Node(key)
        self.capacity += 1
      else:
        head = self.remove_head()
        if head != self.sentinal:
          del self.map[head.val]
          print('hey')
        print('hey')
        node = Node(key)

      self.add_to_tail(node)
      self.map[key] = (value, node)

        

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
