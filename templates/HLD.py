class HLD:
    def __init__(self, tree, root=0):
        self.n = len(tree)
        self.tree = tree
        self.root = root
        self.parent = [-1] * self.n
        self.depth = [0] * self.n
        self.size = [1] * self.n
        self.chain = [i for i in range(self.n)]
        self.pos = [0] * self.n
        self._dfs_size(self.root)
        self._dfs_hld(self.root)

    def _dfs_size(self, u):
        for v in self.tree[u]:
            if v != self.parent[u]:
                self.parent[v] = u
                self.depth[v] = self.depth[u] + 1
                self._dfs_size(v)
                self.size[u] += self.size[v]

    def _dfs_hld(self, u):
        heavy_child = -1
        for v in self.tree[u]:
            if v != self.parent[u] and (heavy_child == -1 or self.size[v] > self.size[heavy_child]):
                heavy_child = v
        if heavy_child != -1:
            self.chain[heavy_child] = self.chain[u]
            self.pos[heavy_child] = self.pos[u] + 1
            self._dfs_hld(heavy_child)
        for v in self.tree[u]:
            if v != self.parent[u] and v != heavy_child:
                self.chain[v] = v
                self.pos[v] = 0
                self._dfs_hld(v)

    def lca(self, u, v):
        while self.chain[u] != self.chain[v]:
            if self.depth[self.chain[u]] < self.depth[self.chain[v]]:
                u, v = v, u
            u = self.parent[self.chain[u]]
        return u if self.depth[u] < self.depth[v] else v