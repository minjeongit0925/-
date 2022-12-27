# 문제
'''
    요세푸스 문제는 다음과 같다.

    1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
    이제 순서대로 K번째 사람을 제거한다. 
    한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
    이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
    원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
    예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

    N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
'''

# 입력
'''
   첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000) 
'''

# 출력
'''
    예제와 같이 요세푸스 순열을 출력한다.
'''

import sys

N, K = map(int, sys.stdin.readline().split())
people = [i for i in range(1, N+1)]
result = []
count = 0

for i in range(len(people)):
    count += K - 1
    if count >= len(people): # 배열의 길이보다 길어지는 것을 방지하기 위한 코드
        count = count % len(people) # 인덱스를 배열의 길이로 나눈 나머지로 바꾼다.
    result.append(people.pop(count))

print("<", end='')
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")

        
# 참고 https://yuna0125.tistory.com/2


'''
    # deque활용한 방법
    # 참고 https://hongcoding.tistory.com/41
    from collections import deque

    queue = deque()
    answer = []

    n, k = map(int, input().split())

    for i in range(1, n+1):
        queue.append(i)

    while queue:
        for i in range(k-1):
            queue.append(queue.popleft())
        answer.append(queue.popleft())

    print("<",end='')
    for i in range(len(answer)-1):
        print("%d, "%answer[i], end='')
    print(answer[-1], end='')
    print(">")
'''