tc = int(input())
rstring = ''
for i in range(tc) :
    R,S = input().split()
    for string in S :
        rstring+=string*int(R)
    print(rstring)
    rstring=''

# n = int(input())
#
# for _ in range(n):
#     a, b = input().split()
#     for i in b:
#         print(i*int(a), end = "")
#     print()