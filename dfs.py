def dfs(g, N):
    visisted = {}
    def dfs_recur(g, node):
        if not node or visisted[node]:
            return
        print(node)
        visisted.add(node)
        adjacents = g[node]
        if not adjacents:
            return
        for v in adjacents:
            dfs_recur(g, v)

    for v in g:
        dfs_recur(g, node)
