# greedy
# 동전의 종류 N, 만들어야 하는 돈 K
# 동전의 가치 ex) 1, 5, 10, 50 ... list
# K원을 만드는데 필요한 동전 개수의 최솟값을 출력해라. 

"""
    내가 입력했던 답 -> 예시에 대한 결과는 잘 나온다.
    오류를 찾지 못했었음.

    N, K = list(map(int, input().split()))
    list = [int(input()) for _ in range(N)]
    count = 0

    for i in range(N):
        if list[N-1-i] >= K:
            continue
        else:
            while True:
                K = K - list[N-1-i]
                count += 1
                if K < list[N-1-i]:
                    break
    print(count)

"""

# 강의에서 나온 답

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()  # 큰 수 부터 파악하기 위한 처리

ans = 0  # 동전 단위를 몇 개 사용했는지 담는 변수

for coin in coins:
    ans += K // coin
    K %= coin

print(ans)

"""
    * 강의에서 나온 답과 내 답의 차이점 *

    1. 나: 큰 수부터 처리하는 것을 배열의 [N-1-i]로 처리함.
       강의: reverse()를 활용해서 큰 수부터 배열을 다시 정렬함.
    2. 나: 뺼셈과 덧셈을 이용해서 동전의 개수를 셈.
       강의: 몫과 나머지를 사용해서 동전의 개수를 더욱 빠르게 셈.

"""