#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.map = {}
        self.size = 0
        self.age = 0
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.age += 1
        self.map[key] = self.age, self.map[key][1]
        return self.map[key][1]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.size < self.c:
                self.map[key] = self.age + 1, value
                self.size += 1
            else:
                del self.map[self.getLeast()[0]]
                self.map[key] = self.age + 1, value
        else: 
            self.map[key] = self.age + 1, value

        self.age += 1
    

    def getLeast(self):
        return min(self.map.items(), key = lambda x: x[1][0])
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

