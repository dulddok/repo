# n = int(input())
#
# fibonachi = [0,1]
#
# for i in range(2,n+1) :
#     num = fibonachi[i-1] + fibonachi[i-2]
#     fibonachi.append(num)
# print(fibonachi[n])

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))