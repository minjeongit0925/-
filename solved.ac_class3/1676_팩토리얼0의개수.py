# 문제
'''
    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
    첫째 줄에 N이 주어진다.
'''

# 출력
'''
    첫째 줄에 구한 0의 개수를 출력한다.
'''

import sys

N = int(sys.stdin.readline())
factorial = 1
num = []
cnt = 0

for i in range(1, N+1):
    factorial = factorial * i

for i in str(factorial):
    num.append(i)

num.reverse()

for i in range(len(num)):
    if num[i] == '0':
        cnt += 1
    else:
        break

print(cnt)

# 5의 배수 10의 배수 1개, 25의 배수 10의 배수 2개, 125의 배수 10의 배수 3개
# 5의 개수 먼저 세고, 25의 개수, 125의 개수를 센다.

'''
    count_5 = N // 5
    count_25 = N // 25
    count_125 = N // 125

    print(count_5 + count_25 + count_125)
'''