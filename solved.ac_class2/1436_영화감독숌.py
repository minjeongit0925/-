# 문제
'''
    N번째 영화의 제목 = N번째로 작은 종말의 숫자
    N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램
'''

# 입력
'''
    숫자 N, N<=10,000
'''

# 출력
'''
    N번째 영화의 제목에 들어간 수
'''

import sys

N = int(sys.stdin.readline())
movie = 666

while N != 0:
    if '666' in str(movie):
        N = N-1
        if N == 0:
            break

    movie = movie + 1

print(movie)

# 숫자를 하나씩 늘려가다가 666이 포함된 숫자가 나오면
# 카운트를 하나 내린다.
# 카운트가 0이 되면 그 숫자를 출력한다.