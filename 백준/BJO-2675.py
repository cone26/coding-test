#문자열 반복
import sys

# 첫째 줄에 테스트 케이스 개수t
t = int(sys.stdin.readline())

for _ in range(t):
    # 반복횟수 r과 문자열 s가 공백으로 구분되어 주어진다.
    [r, s] = sys.stdin.readline().split()
    # 문자열 s를 입력받은 후에
    # 각 문자를 r번 반복해 
    # 새 문자열 p를 만든 후 출력
    for i in s: print(i * int(r), end='')
    print()



