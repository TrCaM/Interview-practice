import heapq

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    MAX_STONES = 1000
    stone_map = [0] * (MAX_STONES + 1)
    for s in stones:
      stone_map[s] += 1

    last_stone = 0

    for s in range(MAX_STONES, 0, -1):
      if stone_map[s]:
        if last_stone:
          break_stones = min(last_stone // s, stone_map[s])
          splited_stone = last_stone - s * break_stones
          stone_map[splited_stone] += 1
          stone_map[s] -= break_stones
          last_stone = splited_stone if splited_stone > s else s * (stone_map[s] % 2)
        else:
          last_stone = s * (stone_map[s] % 2)
        
    return last_stone
  
  def lastStoneWeight2(self, stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
      e1 = heapq.heappop()
      e2 = heapq.heappop()
      if e1 != e2:
        heapq.heappush(- abs(e1 - e2))
    stones.append(0)
    return - stones[0]
  

