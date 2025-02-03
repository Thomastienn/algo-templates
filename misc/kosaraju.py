from collections import defaultdict

def findSCC():
    g = defaultdict(list)
    g_rev = defaultdict(list)
    n = int(input())
    nodes = set()
    
    for _ in range(n):
        a, b = map(int, input().split())
        g[a].append(b)
        g_rev[b].append(a)
        nodes.add(a)
        nodes.add(b)
    
    f = []
    vis = set()
    def dfs1(u):
        vis.add(u)
        for v in g[u]:
            if v not in vis:
                dfs1(v)
        f.append(u)
                
    def dfs2(u, com):
        vis.add(u)
        com.append(u)
        for v in g_rev[u]:
            if v not in vis:
                dfs2(v, com)
                
    for node in nodes:
        if node not in vis:
            dfs1(node)
            
    vis = set()
    scc = []
    while f:
        node = f.pop()
        if node not in vis:
            comp = []
            dfs2(node, comp)
            scc.append(comp)
    
    return scc


print(findSCC())