# BFS queue 자료구조 이용

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], # 인덱싱을 1부터 하기위해 비워둠
    [2,3,8], # 1번 노드와 연결되어있는 노드들
    [1,7], # 2번 노드와 연결되어있는 노드들
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)