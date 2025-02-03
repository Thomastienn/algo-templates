class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graphs = defaultdict(list)
        in_g = defaultdict(int)
        out_g = defaultdict(int)

        ver = set()
        n = len(pairs)
        for u, v in pairs:
            graphs[u].append(v)
            out_g[u] += 1
            in_g[v] += 1
            ver.add(u)
            ver.add(v)

        # Find the first node
        start = 0
        for node in ver:
            if out_g[node] - in_g[node] == 1:
                start = node
                break
            if out_g[node] > 0:
                start = node

        paths = []
        def dfs(node):
            while out_g[node] != 0:
                out_g[node] -= 1
                next_v = graphs[node][-1]
                graphs[node].pop()
                dfs(next_v)
            paths.append(node)

        dfs(start)
        ans = []
        for i in range(len(paths)-1, 0, -1):
            ans.append([paths[i], paths[i-1]])

        return ans
        
# BETTER SOLUTION

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # graph represents adjacency list, inOutDeg tracks in/out degree difference
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        # Build graph and calculate in/out degrees
        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1  # out-degree
            inOutDeg[end] -= 1    # in-degree

        # Find starting node (node with out-degree > in-degree)
        startNode = pairs[0][0]  # default start
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []
        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]
                