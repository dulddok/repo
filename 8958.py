N = int(input())
for i in range(N) :
    ox_list = list(input())
    sum = 0
    plus = 0
    for ox in ox_list :
        if ox == "O" :
            plus +=1
            sum +=plus
        elif ox == "X" :
            plus = 0
    print(sum)


