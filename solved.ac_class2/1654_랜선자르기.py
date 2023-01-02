# 문제
'''
    K개의 랜선
    모두 같은 길이의 N개의 랜선
    손실되는 길이를 없다고 가정.
    최대 랜선의 길이를 구해라.
'''

# 입력
'''
    랜선의 개수 K, 필요한 랜선의 개수 N
'''

# 출력
'''
    N개를 만들 수 있는 랜선의 최대 길이
'''

# 이분탐색을 활용하면 될 것 같다..
K, N = map(int, input().split())
lenList = []

for _ in range(K):
    lenList.append(int(input()))

