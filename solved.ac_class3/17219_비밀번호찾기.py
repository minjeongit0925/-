# 문제
'''
    메모장에서 비밀번호를 찾아주는 프로그램.
'''

# 입력
'''
    사이트 주소의 수 N, 비밀번호를 찾으려는 사이트 주소의 수 M
    N개의 줄에 걸쳐 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다.

    N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 주소가 한줄에 하나씩 입력된다.
'''

# 출력
'''
    첫 번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소의
    비밀번호를 차례대로 각 줄에 하나씩 출력한다.
'''

import sys

sites = set()
pws = set()
findSites = set()

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()
    sites.add(site)
    pws.add(pw)

for _ in range(M):
    findSite = sys.stdin.readline().strip()
    findSites.add(findSite)

