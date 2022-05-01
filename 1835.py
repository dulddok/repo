from collections import deque

N = int(input())
dq = deque()

dq.appendleft(N)

for n in range(N - 1, 0, -1):
    dq.appendleft(n)

    for i in range(n):
        moveCard = dq.pop()
        dq.appendleft(moveCard)

print(*dq)

# from collections import deque
# n = int(input())
# dq = deque()
# dq.append(n)
# a = n
# while len(dq) < n:
#     dq.appendleft(a-1)
#     dq.rotate(a-1)
#     a -= 1
#
# for _ in range(len(dq)):
#     print(dq.popleft(), end=" ")