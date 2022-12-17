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

N, M = map(int, input().split())
for _ in range(M):
    u, v = map(int, input().split())

