# N, K = map(int,input().split())
# cnt = 0
# for i in range(N+1):
#     for j in range(60):
#         for k in range(60):
#             if str(K) in str(i)+str(k)+str(k) :
#                 cnt+=1
#                 print(str(i)+str(k)+str(k))
#
# print(cnt)

n,k = map(int,input().split())
count = 0
k = str(k)
for i in range(n+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for t in range(60):
            if t < 10:
                t = '0' + str(t)
            if k in str(i) + str(j) + str(t):
                count += 1
print(count)