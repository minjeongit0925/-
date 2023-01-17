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

for i in range(1, N+1):
    factorial = factorial * i

