#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = [set() for i in range(n)]
        
        for edge in connections:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        
        output = []
        self.dfs(connections[0][0], connections[0][1], adj_list, {connections[0][0]}, output, {connections[0][0]})
        return output
    
    def dfs(self, prev, node, adj_list, visited, output, prevs):
        visited.add(node)
        visited_adj = set()
        prevs.add(node)
        for adj in adj_list[node]:
            if adj not in visited:
                prevs.add(node)
                visited_adj = visited_adj.union(
                    self.dfs(node, adj, adj_list, visited, output, prevs))
            elif adj != prev and adj in prevs:
                visited_adj.add(adj)

        visited_adj.discard(node)
        if not visited_adj:
            output.append([prev, node])
        prevs.remove(node)
        return visited_adj
            
        
        
# @lc code=end

