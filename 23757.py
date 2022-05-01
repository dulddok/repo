import heapq as hq
#우선 순위 큐는 -가 max -heap 임 - 절댓값
# 어떤 순서로 해도 상관없으나 제거될 때는 가장 큰값이 제거 - max heap
n, m = map(int, input().split())
present = []
for x in list(map(int, input().split())):
    hq.heappush(present, -x)
wish = list(map(int, input().split()))

ispre = False
for i in wish:
    x = -hq.heappop(present)
    if x - i < 0:
        ispre = True
        break
    hq.heappush(present, -(x-i))

if ispre:
    print(0)
else:
    print(1)

# import heapqtest as hq
# n, m = map(int, input().split())
# c = []
# for x in list(map(int, input().split())):
#     hq.heappush(c, -x)
# w = list(map(int, input().split()))
#
# is_neg = False
# for i in w:
#     x = -hq.heappop(c)
#     if x - i < 0:
#         is_neg = True
#         break
#     hq.heappush(c, -(x-i))
#
# if is_neg:
#     print(0)
# else:
#     print(1)