# 문제
'''
    LIFO
    1 부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만든다.
    스택에 push하는 순서는 반드시 오름차순을 지킨다.
    어떤 순서로 push와 pop 연산을 수행해야 하는지 알 수 있다.
'''

# 입력
'''
    n
    1이상 n 이하의 정수가 하나씩 주어짐.
'''

# 출력
'''
    push +
    pop -
    불가능한 경우 NO
'''
# 참고
'''
    https://hongcoding.tistory.com/39
'''

n = int(input())
numList = []
cnt = 1
flag = 0 # 불가능한 경우와 가능한 경우를 나눠주기 위한 플래그
result = []

for _ in range(n):
    num = int(input())
    while cnt <= num:
        numList.append(cnt)
        result.append("+")
        cnt += 1

    if numList[-1] == num:
        numList.pop()
        result.append("-")
    else:
        print("NO") # 불가능한 경우
        flag = 1
        break

if flag == 0: # 가능한 경우
    for i in result:
        print(i)