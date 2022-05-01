# from itertools import combinations
# array = [int(input()) for i in range(9)]
# for res in combinations(array,7) :
#     if sum(res) == 100 :
#         for dwf in res :
#             print(dwf)

# dwfarray = [int(input()) for _ in range(9)]
#
# total = sum(dwfarray)
#
# for i in range(len(dwfarray)) :
#     for j in range(i+1,9) :
#         a = i
#         if total - dwfarray[a] - dwfarray[j] == 100 :
#             for idx in range(9) :
#                 if idx !=a and idx !=j :
#                     print(dwfarray[idx])
#
#

from itertools import combinations
array = [int(input()) for i in range(9)]
for res in combinations(array,7) :
    if sum(res) == 100 :
        for dwf in res :
            print(dwf)
