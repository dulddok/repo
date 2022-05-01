from itertools import permutations, combinations, product,combinations_with_replacement
data = ['a', 'b', 'c']# 데이터 준비# 리스트에서 3개를 뽑아 나열하는 모든 경우를 출력
result = list(permutations(data,3))# 모든 순열 구하기

print(result)

result = list(combinations(data,2))# 2개를 뽑는 모든 조합 구하기

print(result)

result = list(product(data,repeat = 2))# 2개를 뽑는 모든 순열 구하기 (중복 허용)print (result)

result = list(combinations_with_replacement(data,2))# 2개를 뽑는 모든 조합 구하기 (중복 허용)print (result)
