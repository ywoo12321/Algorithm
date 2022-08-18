import sys
from collections import deque
input = sys.stdin.readline
#fun
def dfs(start):
    global visit_dfs, graph, dfs_order
    visit_dfs[start] = True
    dfs_order.append(start)
    for i in graph[start]:
        if visit_dfs[i] == False:
            dfs(i)
    return
def bfs(start):
    global visit_bfs, graph, bfs_order
    queue = deque([start])
    bfs_order.append(start)
    visit_bfs[start] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visit_bfs[i] == False:
                bfs_order.append(i)
                visit_bfs[i] = True
                queue.append(i)
    
#in
vertex_num, edges_num, start_num = map(int,input().split())
edge_li = list(map(int,input().split()) for _ in range(edges_num))
graph = [[] for _ in range(vertex_num+1) ]
for i in range(edges_num):
    edge_li[i] = list(edge_li[i])
for start, end in edge_li:
    graph[start].append(end)
    graph[end].append(start)
for i in graph:
    i.sort()
visit_bfs = [False] * (vertex_num+1)
bfs_order = []
visit_dfs = [False] * (vertex_num+1)
dfs_order = []
#out
bfs(start_num)
dfs(start_num)
print(*dfs_order, sep = ' ')
print(*bfs_order, sep = ' ')