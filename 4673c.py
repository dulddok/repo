# numbers = set(range(1,10001))
# dnum = set()
#
# for i in range(1,10001):
#     for j in str(i) :
#         i += int(j)
#     dnum.add(i)
# snum = sorted(numbers-dnum)
# for i in snum :
#     print(i)
#
result_set = set(range(1,10001))
remove_set = set()

for i in range(1,10001) :
    for j in str(i):
        i = i + int(j)
    remove_set.add(i)
result_set = result_set - remove_set # list 로 할 시 - operland 지원 안함
for n in sorted(result_set):
    print(n)