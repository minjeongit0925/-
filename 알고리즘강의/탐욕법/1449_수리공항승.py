# 가장 왼쪽에서 정수만큼 떨어진 거리만큼 물이 샌다.
# 길이가 L인 테이프 무한개
# 위치의 좌우 0.5만큼 간격을 줘야함.
# 물이 새는 곳 개수 N

"""
    1. 내가 푼 방법
       위치를 오름차순으로 정렬한다.
       시작 지점을 첫번쨰 포인트로 잡는다.
       주어진 위치의 두번째 지점부터 테이프의 길이의 범위 안에 들어 있다면, 넘어간다.
       범위를 벗어난다면, 테이프 수를 하나 증가한다. 

        N, L = map(int, input().split())
        leakSpots = list(map(int, input().split()))

        leakSpots.sort()

        startPoint = leakSpots[0]
        count = 1

        for leakSpot in leakSpots[1:]:
            if leakSpot in range(startPoint, startPoint + L):
                continue
            else:
                startPoint = leakSpot
                count += 1

        print(count)

"""

"""
    2. 강의 설명 -> 길이가 1000개인 배열을 활용하는 방법 
"""
N, L = map(int, input().split())
coord = [False] * 1001  # 1001개의 False로 이루어진 배열

# 새는 곳의 위치가 True로 바뀐다. 
for i in map(int, input().split()):
    coord[i] = True 

x = 0  # 현재 살펴 보고 있는 좌표
ans = 0  # 테이프 몇 개 사용했는지 파악할 변수
while x < 1001:
    if coord[x]:
        ans += 1 
        x += L
    else:
        x += 1

print(ans)
    