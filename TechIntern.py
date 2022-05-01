def solution(s):
    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(table)):
        s = s.replace(table[i], str(i))

    return int(s)
N = input()
#intlist = ['0','1','2','3','4','5','6','7','8','9']
print(int(solution(N)))