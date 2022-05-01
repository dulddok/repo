while True:
    B,N = map(int,input().split())
    A =0
    if B ==0 and N==0 :
        break
    A = 0
    while A ** N < B :
        A +=1
        if A**N ==B:
            break
        if A**N >B and A**N !=B :
            if (A**N) -B < B-((A-1)**N) :
                A=A
                break
            else :
                A -=1
                break
    print(A)



# while 1:
#     B, N = map(int, input().split())
#     if B == N == 0:
#         break
#     i = 0
#     while i**N < B:
#         i += 1
#     print(i if i**N-B < B-(i-1)**N else i-1)