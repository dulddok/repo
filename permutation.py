from itertools import permutations,combinations

data = ['a','b','c']
result = list(permutations(data,3))
# 3개를 나열하는 모든 순열

result2 = list(combinations(data,2))
#2개를 뽑느 모든 조합

print(result)
print(result2)