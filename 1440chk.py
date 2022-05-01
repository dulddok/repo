# # 타임머신
# import sys
#
# times = list(map(int, sys.stdin.readline().split(":")))
# print(times[0:])
# times_list = []
# for i in range(3):
#     for j in range(2):
#         make_time = list(times)
#         new_times = [make_time.pop(i)]
#         new_times.append(make_time.pop(j))
#         new_times.append(make_time.pop(0))
#         times_list.append(new_times)
#
# cnt = 0
# for i, j, h in times_list:
#     if 1 <= i <= 12 and 0 <= j <= 59 and 0 <= h <= 59:
#         cnt += 1
#
# print(cnt)
from itertools import permutations
perms = list(permutations(map(int,input().split(":"))))
cnt = 0
for perm in perms:
    if perm in perms:
        if 1 <= perm[0] <= 12 and 0 <= perm[1] <= 59 and 0 <= perm[2] <=59 :
            cnt+=1
        print(perm)

print(cnt)
## 해당 내용으로 한 이유는 어떤게 시가 되든지 상관없이 편의상 첫번째 자리수를 시간이라고 두면 첫번째 perm0 자리에 시간 두고
## 둘째부터 분초로 0에서 59 들어가는지 확인해주면 된다.