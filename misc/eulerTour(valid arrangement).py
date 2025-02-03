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
                