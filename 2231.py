n = int(input())

for i in range(1, n+1):
    a = sum(list(map(int, str(i))))
    s = i + a

    if s == n:
        print(i)
        quit()

print(0)
