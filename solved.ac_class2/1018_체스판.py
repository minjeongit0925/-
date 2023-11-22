# 문제
'''
    NXM 체스판
    => 8X8 체스판으로 잘라서 수정
    맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
    지민이가 다시 칠해야 하는 정사각형의 최소 개수
'''

# 입력
'''
    N, M
    보드의 각 행의 상태 B는 검은색, W는 흰색
'''

# 출력
'''
    다시 칠해야 하는 정사각형 개수의 최솟값
'''

"""
    M행 N열을 검색하면서 8X8로 나눈다.
    처음이 B일경우, W일 경우 나눈다.
    전이 B 인데 다음이 B일 경우 W로 바꾼다.
    [참고] https://ittrue.tistory.com/60
"""

N, M = map(int, input().split())
chess = []
result = []

for _ in range(N):
    chess.append(input())


for n in range(N-7):
    for m in range(M-7):
        W_first = 0
        B_first = 0
        for i in range(n, n+8):
            for j in range(m, m+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'B':
                        B_first += 1
                    if chess[i][j] != 'W':
                        W_first += 1
                else:
                    if chess[i][j] != 'W':
                        B_first += 1
                    if chess[i][j] != 'B':
                        W_first += 1

        result.append(B_first)
        result.append(W_first)

print(min(result))

