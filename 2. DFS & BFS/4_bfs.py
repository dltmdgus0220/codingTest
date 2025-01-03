"""
문제: 미로 탈출
* 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의
괴물이 있어 이를 피해 탈출해야 합니다.
* 동빈이의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩
이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어
있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
* 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는
시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
"""

from collections import deque

def check(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        False
    return True

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0,1))
    while queue:
        x, y, count = queue.popleft()
        if x == n-1 and y == m-1:
            return count
        for i in range(4):
            if check(x+dx[i], y+dy[i]) == True:
                graph[x][y] = 0
                queue.append((x+dx[i], y+dy[i], count+1))


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs())

# graph 노드 값을 움직인 횟수로 바꾸는 방법도 있음
# https://github.com/ndb796/python-for-coding-test/blob/master/5/11.py