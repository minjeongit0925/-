# 이차원 배열
# H * W => HW ex) H=6, W=12 612호가 최고
# 1번째 손님 => 101
# 2번째 손님 => 201
# W가 1인 경우를 모두 점령한 뒤, 2인 경우를 생각한다.
floor = 0
roomNum = 0

T = int(input())  # testcase 수
for _ in range(T):
    H, W, N = map(int, input().split())
    # H = 층수, W = 한 층에 방 갯수, N = N번째 손님

    floor = N % H
    roomNum = N // H + 1

    if N % H == 0:
        roomNum = N // H
        floor = H
    print(floor*100+roomNum)
