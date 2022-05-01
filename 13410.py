A,B = map(int,input().split())

rgugu = []
for i in range(1,B+1):
    rgugu.append(int(str(A*i)[::-1]))

print(max(rgugu))





