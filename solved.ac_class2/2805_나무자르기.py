# 문제
'''
    나무 M미터 필요함.
    절단기에 높이 H 지정.
    적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 구하시오.
'''

# 입력
'''
    나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
    나무의 높이
'''

# 출력
'''
    적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''
# 이분탐색의 기본
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1 # 시작
end = sum(trees) # 끝

while start <= end: # 시작이 끝보다 작을 때까지
    mid = (start + end) // 2 # 중간값
    cnt = 0 # 나무의 길이 판단

    for tree in trees: # trees 배열에서
        if tree > mid: # 중간값보다 크면
            cnt += tree - mid # 나무의 길이에 더하기
    if cnt >= M: # 원하는 나무의 길이보다 크면
        start = mid + 1 # 시작에 중간값 + 1 해서 다시 시작
    else:
        end = mid - 1 # 그 외에는 끝에서 중간값 -1 해서 다시 시작
print(end)