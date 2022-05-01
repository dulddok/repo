# dwfarray = [int(input()) for _ in range(9)]
#
# total = sum(dwfarray)
# sortdwf = []
# for i in range(len(dwfarray)) :
#     for j in range(i+1,9) :
#         a = i
#         if total - dwfarray[a] - dwfarray[j] == 100 :
#             for idx in range(9) :
#                 if idx !=a and idx !=j :
#                      # print(dwfarray[idx])
#                     sortdwf.append(dwfarray[idx])
#
# sortdwf = sorted(sortdwf)
# print(sortdwf)
#
# for sdwf in sortdwf:
#     print(sdwf)

# 1번째 방법 (temp, remove)

n = 9
temp1, temp2 = 0, 0
arr = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            temp1 = arr[i]
            temp2 = arr[j]

arr.remove(temp1)
arr.remove(temp2)

print('\n'.join(map(str, sorted(arr))))