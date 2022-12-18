# 문제
'''
    방향 없는 그래프가 주어졌을떄, 연결 요소의 개수
'''

# 입력
'''
    정점의 개수 N, 간선의 개수 M
    양 끝점 u, v  
'''

# 출력
'''
    연결 요소의 개수
'''

from collections import deque

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u][v] = 1

def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(N):
            if adj[now][nxt]:
                dq.append(nxt)
    print(dq)

bfs()