alphabet = input()

alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpahindex = []

idx = 0


for alpha in alphalist :
    if alpha in alphabet :
        idx = alphabet.index(alpha)
        alpahindex.append(idx)
    elif alpha not in alphabet :
        idx = -1
        alpahindex.append(idx)
for i in range(len(alpahindex)) :
    print(alpahindex[i],end=" ")



# s = input()
#
# alphbet = "abcdefghijklmnopqrstuvwyz"
#
# for i in alphbet:
#     if i in s:
#         print(s.index(i),end=" ")
#     else :
#         print(-1, end=" ")