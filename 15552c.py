import sys
N  = int(input())
input = sys.stdin.readline
for i in range(N):
    A,B = map(int,input().split())
    print(A+B)